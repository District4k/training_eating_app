from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base




class SectorModel(Base):
    __tablename__ = 'sector_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sector_name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('sector_model.id', ondelete='CASCADE'), nullable=True)

    # Relationship for hierarchical structure
    parent = relationship("SectorModel", remote_side=[id], backref="children")

    def to_dict(self, exclude_fields=None):
        """
        Converts the model instance to a dictionary.
        :param exclude_fields: List of fields to exclude from the dictionary.
        :return: Dictionary representation of the model.
        """
        exclude_fields = exclude_fields or []
        data = {
            "id": self.id,
            "sector_name": self.sector_name,
            "parent_id": self.parent_id,
            "children": [child.id for child in self.children],  # Avoid full recursion for children
        }
        # Remove excluded fields
        for field in exclude_fields:
            data.pop(field, None)
        return data