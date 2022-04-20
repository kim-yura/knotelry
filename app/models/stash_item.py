from .db import db
from datetime import datetime


class Stash_Item_Image(db.Model):
    __tablename__ = 'stash_item_images'

    id = db.Column(db.Integer, primary_key=True)
    stash_item_id = db.Column(db.Integer, db.ForeignKey('stash.id'))
    image_url = db.Column(db.String(100))

    stash_item = db.relationship('Stash_Item', back_populates='stash_item_image')

    def to_dict(self):
        return {
            'id': self.id,
            'stash_item_id': self.stash_item_id,
            'image_url': self.image_url,
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'stashItemId': self.stash_item_id,
            'imageURL': self.image_url,
        }


class Stash_Item(db.Model):
    __tablename__ = 'stash'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(50))
    status = db.Column(db.String(50))

    acquired = db.Column(db.DateTime)
    acquired_from = db.Column(db.Text)
    acquired_price = db.Column(db.Float)
    acquired_currency = db.Column(db.String(5))

    # Broader attributes
    colors = db.Column(db.Text)

    # Fiber and yarn attributes
    dyer_name = db.Column(db.Text)
    colorway_name = db.Column(db.Text)
    fiber_content = db.Column(db.String(200))

    # Fiber attributes
    fiber_quantity = db.Column(db.Float)
    fiber_quantity_unit = db.Column(db.String(5))

    # Yarn attributes
    yarn_weight = db.Column(db.String(20))
    length_per_skein = db.Column(db.Float)
    length_unit = db.Column(db.String(5))
    weight_per_skein = db.Column(db.Float)
    weight_unit = db.Column(db.String(5))
    skeins_stashed = db.Column(db.Float)
    length_stashed = db.Column(db.Float)
    weight_stashed = db.Column(db.Float)
    is_handspun = db.Column(db.Boolean)

    notes = db.Column(db.Text)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user = db.relationship('User', back_populates='stash_item')
    stash_item_image = db.relationship('Stash_Item_Image', back_populates='stash_item')
    project_material = db.relationship('Project_Material', back_populates='stash_item')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'type': self.type,
            'status': self.status,

            'acquired': self.acquired,
            'acquired_from': self.acquired_from,
            'acquired_price': self.acquired_price,
            'acquired_currency': self.acquired_currency,

            'colors': self.colors,

            'dyer_name': self.dyer_name,
            'colorway_name': self.colorway_name,
            'fiber_content': self.fiber_content,

            'fiber_quantity': self.fiber_quantity,
            'fiber_quantity_unit': self.fiber_quantity_unit,

            'yarn_weight': self.yarn_weight,
            'length_per_skein': self.length_per_skein,
            'length_unit': self.length_unit,
            'weight_per_skein': self.weight_per_skein,
            'weight_unit': self.weight_unit,
            'skeins_stashed': self.skeins_stashed,
            'length_stashed': self.length_stashed,
            'weight_stashed': self.weight_stashed,
            'is_handspun': self.is_handspun,

            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at,

            'user': self.user.to_dict(),
            'stash_item_images': [image.to_dict() for image in self.stash_item_image],
            # 'projects': self.project_material.to_dict(),
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'title': self.title,
            'description': self.description,
            'type': self.type,
            'status': self.status,

            'acquired': self.acquired,
            'acquiredFrom': self.acquired_from,
            'acquiredPrice': self.acquired_price,
            'acquiredCurrency': self.acquired_currency,

            'colors': self.colors,

            'dyerName': self.dyer_name,
            'colorwayName': self.colorway_name,
            'fiberContent': self.fiber_content,

            'fiberQuantity': self.fiber_quantity,
            'fiberQuantityUnit': self.fiber_quantity_unit,

            'yarnWeight': self.yarn_weight,
            'lengthPerSkein': self.length_per_skein,
            'lengthUnit': self.length_unit,
            'weightPerSkein': self.weight_per_skein,
            'weightUnit': self.weight_unit,
            'skeinsStashed': self.skeins_stashed,
            'lengthStashed': self.length_stashed,
            'weightStashed': self.weight_stashed,
            'isHandspun': self.is_handspun,

            'notes': self.notes,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,

            'user': self.user.to_JSON(),
            'stashItemImages': [image.to_JSON() for image in self.stash_item_image],

            # 'projects': self.project_material.to_JSON(),
        }
