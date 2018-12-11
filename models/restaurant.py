from db import db


class RestaurantModel(db.Model):
    __tablename__ = "restaurants"

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(80))
    location    = db.Column(db.String(80))
    address     = db.Column(db.String(100))
    rating      = db.Column(db.Float(precision=2))
    google_id   = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, location, address, rating, google_id):
        self.name = name
        self.location = location
        self.address = address
        self.rating = rating
        self.google_id = google_id

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "address": self.address,
            "rating": self.rating,
            "google_id": self.google_id,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
