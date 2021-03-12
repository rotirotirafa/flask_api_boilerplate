from src.db import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(50))
    status = db.Column(db.String(10))

    def __init__(self, user_id, username, email, password, status):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.status = status

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'status': self.status
        }

    @classmethod
    def find_by_id(cls, _id):
        user = cls.query.filter_by(_id=_id).first()
        if user:
            return user
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, email, password):
        self.email = email
        self.password = password

    def delete(self):
        db.session.delete(self)
        db.session.commit()
