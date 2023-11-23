from infrastructure.db import db
from sqlalchemy import Enum
from core.user.constants import UserRole


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(Enum(UserRole), default=UserRole.JOB_SEEKER, nullable=False)