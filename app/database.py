#!/usr/bin/env python3
"""
This module sets up the SQLAlchemy engine, session,
and base class for the application's ORM.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Config

# Create the SQLAlchemy engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Session instance to be used across the application
Session = SessionLocal

# Base class for the ORM models
Base = declarative_base()

