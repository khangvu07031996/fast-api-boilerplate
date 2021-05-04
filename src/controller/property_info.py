from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import deps
from src.service.property_info_service import PropertyInfoService
from src.repository import PropertyRepository
from src.cqrs.queries import PropertyInfoQueryImpl
router = APIRouter(prefix="/property_info")


def property_info_query(db: Session = Depends(deps.get_db)) -> PropertyInfoQueryImpl:
    property_repository: PropertyRepository = PropertyRepository(db)
    return PropertyInfoQueryImpl(property_repository)


@router.get("/property_detail/{property_id}")
async def test(
    *,
    property_info_query_instance: PropertyInfoQueryImpl = Depends(property_info_query),
    property_id,
):
    return await property_info_query_instance.find_property_info(property_id)
