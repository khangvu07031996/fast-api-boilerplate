from pydantic import BaseModel, Field
from typing import Any


class PropertyInfoQuery(BaseModel):
    property_id: str = Field(example="6759791608465457152")
