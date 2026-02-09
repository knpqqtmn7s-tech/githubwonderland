from fastapi import APIRouter, status
from schemas.game_schema import GameCreate
from controllers.game_controller import get_games, create_game

router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/", status_code=status.HTTP_200_OK)
def list_games():
    return get_games()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_game(game: GameCreate):
    return create_game(game)
