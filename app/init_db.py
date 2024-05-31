#!/usr/bin/env python3
import json
from sqlalchemy.orm import Session
from .database import engine, Base
from .models import Category, Article


def init_db():
    """
    Initialize the database with default categories,
    and articles from JSON file.
    """
    Base.metadata.create_all(bind=engine)

    session = Session(bind=engine)

    with open('db_data.json', 'r') as file:
        default_data = json.load(file)

    categories_data = default_data.get('categories', [])
    for category_data in categories_data:
        category = session.query(Category).filter_by(
            name=category_data['name']).first()
        if not category:
            category = Category(name=category_data['name'])
            session.add(category)

    articles_data = default_data.get('articles', [])
    for article_data in articles_data:
        category_name = article_data['category']
        category = session.query(Category).filter_by(
            name=category_name).first()
        if category:
            article = session.query(Article).filter_by(
                title=article_data['title']).first()
            if not article:
                photo_url = article_data['photo_url']
                if photo_url.startswith('/blog/article/'):
                    photo_url = photo_url[len('/static/'):]
                article = Article(
                    title=article_data['title'],
                    content=article_data['content'],
                    category=category,
                    photo_url=photo_url
                )
                session.add(article)

    session.commit()
    session.close()


def reset_db():
    """
    Reset the database by dropping all tables and recreating them.
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    init_db()
