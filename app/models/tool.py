from .db import db
from datetime import datetime


class Tool(db.Model):
    __tablename__ = 'tools'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    acquired = db.Column(db.DateTime)
    status = db.Column(db.String(50))
    favorited = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    for_spinning = db.Column(db.Boolean, nullable=False, default=False)
    for_weaving = db.Column(db.Boolean, nullable=False, default=False)
    for_knitting = db.Column(db.Boolean, nullable=False, default=False)
    for_crocheting = db.Column(db.Boolean, nullable=False, default=False)
    for_sewing = db.Column(db.Boolean, nullable=False, default=False)
    for_embroidery = db.Column(db.Boolean, nullable=False, default=False)

    image_url = db.Column(db.String(100))

    user = db.relationship('User', back_populates='tool')
    project_tool = db.relationship('Project_Tool', back_populates='tool')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'acquired': self.acquired,
            'status': self.status,
            'favorited': self.favorited,
            'created_at': self.created_at,
            'updated_at': self.updated_at,

            'for_spinning': self.for_spinning,
            'for_weaving': self.for_weaving,
            'for_knitting': self.for_knitting,
            'for_crocheting': self.for_crocheting,
            'for_sewing': self.for_sewing,
            'for_embroidery': self.for_embroidery,

            'image_url': self.image_url,
            'user': self.user.to_dict(),
            'projects': self.project_tool.to_dict(),
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'title': self.title,
            'description': self.description,
            'acquired': self.acquired,
            'status': self.status,
            'favorited': self.favorited,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,

            'forSpinning': self.for_spinning,
            'forWeaving': self.for_weaving,
            'forKnitting': self.for_knitting,
            'forCrocheting': self.for_crocheting,
            'forSewing': self.for_sewing,
            'forEmbroidery': self.for_embroidery,

            'imageURL': self.image_url,
            'user': self.user.to_JSON(),
        }
