#!/usr/bin/env python3
"""
This module defines the ORM models for Category and Article using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Category(Base):
    """
    ORM model for the 'categories' table.
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    articles = relationship('Article', back_populates='category')

    def __repr__(self):
        """
        String representation of the Category model.
        """
        return f"<Category(name='{self.name}')>"

class Article(Base):
    """
    ORM model for the 'articles' table.
    """
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='articles')
    photo_url = Column(String)

    def __repr__(self):
        """
        String representation of the Article model.
        """
        return f"<Article(title='{self.title}', content='{self.content}')>"
