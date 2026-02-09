from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.game_routes import router as game_router
from routes.article_routes import router as article_router

app = FastAPI()

app.include_router(user_router)
app.include_router(game_router)
app.include_router(article_router)
