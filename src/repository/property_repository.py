from sqlalchemy.orm import Session
from src.models.property import Property


class PropertyRepository:
    def find_property_by_id(self, db: Session, id) -> Property:
        return db.query(Property).filter(Property.id == id).first()