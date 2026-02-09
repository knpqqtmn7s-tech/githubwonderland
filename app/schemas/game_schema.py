from pydantic import BaseModel
from datetime import date

class GameCreate(BaseModel):
    title: str
    releaseDate: date

class GameResponse(GameCreate):
    gameId: int
