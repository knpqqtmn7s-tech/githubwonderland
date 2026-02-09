from pydantic import BaseModel

class ArticleCreate(BaseModel):
    title: str
    content: str
    userId: int
    gameId: int

class ArticleResponse(ArticleCreate):
    articleId: int
