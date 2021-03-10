from src.db import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(50))
    status = db.Column(db.String(10))

    def __init__(self, user_id, username, email, password):
        self.user_id = user_id,
        self.username = username,
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }