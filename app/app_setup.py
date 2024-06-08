#!/usr/bin/env python3
"""
This module sets up the Flask application,
including configuration, database 
initialization, and session management.
"""
from flask import Flask
from .config import Config
from .database import engine, Base
from .init_db import reset_db
from flask import g


def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database
    Base.metadata.create_all(bind=engine)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        Close the database session at the end of the request.
        """
        session = getattr(g, '_session', None)
        if session is not None:
            session.close()

    # Reset the database (this will drop and recreate all tables)
    reset_db()

    return app
