from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.ext.db import db


class User(db.Model):
    __tablename__ = "users"
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, _id, email, password):
        self._id = _id
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'user_id': self._id,
            'email': self.email
        }

    @classmethod
    def find_by_id(cls, _id):
        user = cls.query.filter_by(_id=_id).first()
        if user:
            return user.to_dict()
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


class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    police_check = db.Column(db.String)
    driver_licence = db.Column(db.String)
    veichle_plate_number = db.Column(db.String)
    veichle_model = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey(User._id))


class Traveler(db.Model):
    __tablename__ = "travelers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    police_check = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey(User._id))


class Trip(db.Model):
    __tablename__ = "trips"
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, ForeignKey(Driver.id))
    destination_a = db.Column(db.String)
    destination_b = db.Column(db.String)

    #driver = relationship('Driver', remote_side='Driver._id', foreign_keys='driver.id')


class Match(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver_id = db.Column(db.Integer, ForeignKey(Driver.id))
    traveler_id = db.Column(db.Integer, ForeignKey(Traveler.id))
    trip_id = db.Column(db.Integer, ForeignKey(Trip.id))

    #driver = relationship('Driver', remote_side='Driver._id', foreign_keys='driver.id')
    #traveler = relationship('Traveler',  remote_side='Traveler._id', foreign_keys='traveler.id')
    #trip = relationship('Trip',  remote_side='Trip._id', foreign_keys='trip.id')


