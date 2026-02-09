from data.fake_db import articles_db

def get_articles():
    return articles_db

def create_article(article_data):
    new_article = {
        "articleId": len(articles_db) + 1,
        "title": article_data.title,
        "content": article_data.content,
        "userId": article_data.userId,
        "gameId": article_data.gameId
    }
    articles_db.append(new_article)
    return new_article
