from .db import db
from datetime import datetime


class Group_Membership(db.Model):
    __tablename__ = 'group_memberships'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    group = db.relationship('Group', back_populates='group_membership')
    user = db.relationship('User', back_populates='group_membership')

    def to_dict(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'user_id': self.user_id,

            'group': self.group.to_dict(),
            'user': self.user.to_dict(),
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'groupId': self.group_id,
            'userId': self.user_id,

            'group': self.group.to_JSON(),
            'user': self.user.to_JSON(),
        }


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    craft_types = db.Column(db.String(50))
    country = db.Column(db.String(2))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    moderator_ids = db.Column(db.Text)

    group_membership = db.relationship('Group_Membership', back_populates='group')
    owner = db.relationship('User', back_populates='group_owner')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'craft_types': self.craft_types,
            'country': self.country,
            'owner_id': self.owner_id,
            'moderator_ids': self.moderator_ids,

            'group_membership': self.group_membership.to_dict(),
            'owner': self.owner.to_dict(),
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'craftTypes': self.craft_types,
            'country': self.country,
            'ownerId': self.owner_id,
            'moderatorIds': self.moderator_ids,

            'groupMembership': self.group_membership.to_JSON(),
            'owner': self.owner.to_JSON(),
        }
