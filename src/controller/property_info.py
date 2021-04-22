from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import deps
from src.service.property_info_service import PropertyInfoService
router = APIRouter(prefix="/property_info")


@router.get("/property_detail/{property_id}")
async def test(
    *,
    db: Session = Depends(deps.get_db),
    property_id,
):
    return PropertyInfoService(db).find_property_by_id(id=property_id)
