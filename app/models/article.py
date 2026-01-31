from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base
from app.models.enums import ArticleStatus

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)

    status = Column(
        Enum(ArticleStatus),
        nullable=False,
        default=ArticleStatus.DRAFT
    )

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    game_id = Column(
        Integer,
        ForeignKey("games.id"),
        nullable=False
    )

    author = relationship("User", back_populates="articles")
    game = relationship("Game", back_populates="articles")
