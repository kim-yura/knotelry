from .db import db
from datetime import datetime



class Gallery_Photo(db.Model):
    __tablename__ = 'gallery_photos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user = db.relationship('User', back_populates='gallery_photo')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'image_url': self.image_url,
            'created_at': self.created_at,

            'user': self.user.to_dict()
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'imageURL': self.image_url,
            'createdAt': self.created_at,

            'user': self.user.to_JSON()
        }
