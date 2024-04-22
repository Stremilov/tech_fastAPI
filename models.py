from typing import List, Type

from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///tech.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    registration_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}, {self.username}, {self.email}, {self.registration_date}"


