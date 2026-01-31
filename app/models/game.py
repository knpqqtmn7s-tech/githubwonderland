# app/models/game.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    release_date = Column(Date)

    genre_id = Column(
        Integer,
        ForeignKey("genres.id"),
        nullable=False
    )

    developer_id = Column(
        Integer,
        ForeignKey("developers.id"),
        nullable=False
    )

    publisher_id = Column(
        Integer,
        ForeignKey("publishers.id"),
        nullable=False
    )

    genre = relationship("Genre", back_populates="games")
    developer = relationship("Developer", back_populates="games")
    publisher = relationship("Publisher", back_populates="games")
    articles = relationship("Article", back_populates="game")
