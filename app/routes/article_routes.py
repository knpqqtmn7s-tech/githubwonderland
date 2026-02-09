from fastapi import APIRouter, status
from schemas.article_schema import ArticleCreate
from controllers.article_controller import get_articles, create_article

router = APIRouter(prefix="/articles", tags=["Articles"])

@router.get("/", status_code=status.HTTP_200_OK)
def list_articles():
    return get_articles()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_article(article: ArticleCreate):
    return create_article(article)
