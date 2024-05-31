#!/usr/bin/env python3

class Config:
    """
    Configuration class for the Flask application.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # SQLite URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
