#!/usr/bin/env python3
from flask import Flask, render_template, g
from .config import Config
from .database import engine, SessionLocal, Base
from .routes.main import main_bp
from .routes.blog import blog_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp)

    # Database initialization code
    Base.metadata.create_all(bind=engine)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session = getattr(g, '_session', None)
        if session is not None:
            session.close()

    return app
