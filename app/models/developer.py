from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base

class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    country = Column(String(50))

    games = relationship("Game", back_populates="developer")
