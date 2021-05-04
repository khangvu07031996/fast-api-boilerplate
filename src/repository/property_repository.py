from abc import ABC
from sqlalchemy.orm import Session
from src.models.property import Property
from typing import Optional


class PropertyRepository(ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    async def find_property_by_id(self, property_id: str) -> Optional[Property]:
        return self.db.query(Property).filter(Property.id == property_id).first()
