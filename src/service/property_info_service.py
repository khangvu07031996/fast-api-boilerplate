from src.service.base import BaseService
from src.repository.property_repository import PropertyRepository


class PropertyInfoService(BaseService):
    def find_property_by_id(self, id):
        return PropertyRepository().find_property_by_id(db=self.db, id=id)