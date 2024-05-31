#!/usr/bin/env python3
from flask import Flask
from .config import Config
from .database import engine, SessionLocal, Base
from .init_db import reset_db
from flask import g


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Base.metadata.create_all(bind=engine)

    def shutdown_session(exception=None):
        session = getattr(g, '_session', None)
        if session is not None:
            session.close()

    reset_db()

    return app
