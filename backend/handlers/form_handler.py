import json
from models.user_model import UserModel
from models.sector_model import SectorModel
from handlers.base_handler import BaseHandler


class FormHandler(BaseHandler):
    def post(self):
        # Set response content type
        self.set_header("Content-Type", "application/json")

        try:
            # Parse JSON body
            try:
                data = json.loads(self.request.body)
            except json.JSONDecodeError:
                self.set_status(400)
                self.write(json.dumps({"status": "error", "message": "Invalid JSON format"}))
                return

            # Extract individual fields
            name = data.get("name")
            sectors = data.get("sectors")
            terms = data.get("terms")

            # Validate required fields
            if not name or not isinstance(name, str):
                raise ValueError("Name is required and must be a string.")
            if not isinstance(sectors, list):
                raise ValueError("Sectors must be a list.")
            if terms is None or not isinstance(terms, bool):
                raise ValueError("Terms must be a boolean.")

            # Validate that all sector IDs exist in the database
            valid_sectors = (
                self.db.query(SectorModel.id)
                .filter(SectorModel.id.in_(sectors))
                .filter(SectorModel.parent_id.isnot(None))  # Exclude rows where parent_id is NULL
                .all()
            )
            valid_sectors = {sector.id for sector in valid_sectors}

            invalid_sectors = set(sectors) - valid_sectors
            if invalid_sectors:
                raise ValueError(f"The following sectors are invalid: {list(invalid_sectors)}")

            # Convert sectors list to a comma-separated string
            sectors_csv = ",".join(map(str, sectors))

            # Check if the user with the same name already exists
            existing_user = self.db.query(UserModel).filter(UserModel.name == name).first()

            if existing_user:
                # Update existing user
                existing_user.sectors = sectors_csv
                existing_user.terms = terms
                self.db.commit()  # Commit the changes
                self.write(json.dumps({"status": "success", "message": "Data updated successfully"}))
            else:
                # Create new user entry if not found
                saving_entry = UserModel(name=name, sectors=sectors_csv, terms=terms)
                self.db.add(saving_entry)
                self.db.commit()
                self.write(json.dumps({"status": "success", "message": "Data saved successfully"}))

        except ValueError as e:
            self.set_status(400)
            self.write(json.dumps({"status": "error", "message": str(e)}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"status": "error", "message": "Internal server error", "details": str(e)}))
