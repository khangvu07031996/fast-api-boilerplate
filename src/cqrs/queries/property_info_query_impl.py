from abc import ABC
from src.repository.property_repository import PropertyRepository


class PropertyInfoQueryImpl(ABC):
    def __init__(self, property_repository: PropertyRepository):
        self.property_repository: PropertyRepository = property_repository

    async def find_property_info(self, property_id: str):
        try:
            return await self.property_repository.find_property_by_id(property_id)
        except:
            raise