from src.core.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Property(Base):
    __tablename__ = "property"
    name = Column(String)
    __table_args__ = {'schema': 'hotel'}
