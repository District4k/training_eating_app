from tornado.escape import json_encode
from handlers.base_handler import BaseHandler
from models.sector_model import SectorModel


class LoadSectorsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # Query all sectors
        sectors = self.db.query(SectorModel).all()

        # Convert each SectorModel instance to a dictionary
        sectors_dict = [sector.to_dict(exclude_fields=["children", "parent"]) for sector in sectors]

        # Build the hierarchical structure
        hierarchy = build_sector_hierarchy(sectors_dict, parent_id=None)

        # Write the JSON response
        self.set_header("Content-Type", "application/json")
        self.write(json_encode(hierarchy))


def build_sector_hierarchy(sectors, parent_id):
    """
    Recursively build a hierarchical tree structure from flat sector data.

    :param sectors: List of sector dictionaries.
    :param parent_id: The ID of the parent sector for the current level.
    :return: List representing the hierarchical tree.
    """
    hierarchy = []
    for sector in sectors:
        if sector.get("parent_id") == parent_id:
            node = {
                "id": sector["id"],
                "sector_name": sector["sector_name"],
                "parent_id": sector["parent_id"],
            }
            # Recursively find children
            children = build_sector_hierarchy(sectors, sector["id"])
            if children:
                node["children"] = children
            hierarchy.append(node)
    return hierarchy
