#!/usr/bin/env python3
""" This script initializes and runs the Flask web application."""
from app.app_setup import create_app
from app.init_db import reset_db
from app import create_app


app = create_app()


if __name__ == "__main__":
    reset_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
