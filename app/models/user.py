from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_pic_url = db.Column(db.String(500), default='https://knotelry.s3.amazonaws.com/profilepic_default.png')
    bio = db.Column(db.Text)
    crafting_journey = db.Column(db.Text)
    roles = db.Column(db.Text)
    pronouns_she = db.Column(db.Boolean, nullable=False, default=False)
    pronouns_he = db.Column(db.Boolean, nullable=False, default=False)
    pronouns_they = db.Column(db.Boolean, nullable=False, default=False)
    pronouns_custom = db.Column(db.String(30))

    instagram = db.Column(db.String(30))
    twitter = db.Column(db.String(50))
    kofi = db.Column(db.String(100))
    website = db.Column(db.String(300))

    is_spinner = db.Column(db.Boolean, nullable=False, default=False)
    is_weaver = db.Column(db.Boolean, nullable=False, default=False)
    is_knitter = db.Column(db.Boolean, nullable=False, default=False)
    is_crocheter = db.Column(db.Boolean, nullable=False, default=False)
    is_sewist = db.Column(db.Boolean, nullable=False, default=False)
    is_embroiderer = db.Column(db.Boolean, nullable=False, default=False)

    tool = db.relationship('Tool', back_populates='user')
    gallery_photo = db.relationship('Gallery_Photo', back_populates='user')
    stash_item = db.relationship('Stash_Item', back_populates='user')
    project = db.relationship('Project', back_populates='user')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile_pic_url': self.profile_pic_url,
            'bio': self.bio,
            'crafting_journey': self.crafting_journey,
            'roles': self.roles,
            'pronouns_she': self.pronouns_she,
            'pronouns_he': self.pronouns_he,
            'pronouns_they': self.pronouns_they,
            'pronouns_custom': self.pronouns_custom,

            'instagram': self.instagram,
            'twitter': self.twitter,
            'kofi': self.kofi,
            'website': self.website,

            'is_spinner': self.is_spinner,
            'is_weaver': self.is_weaver,
            'is_knitter': self.is_knitter,
            'is_crocheter': self.is_crocheter,
            'is_sewist': self.is_sewist,
            'is_embroiderer': self.is_embroiderer
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profilePicUrl': self.profile_pic_url,
            'bio': self.bio,
            'craftingJourney': self.crafting_journey,
            'roles': self.roles,
            'pronounsShe': self.pronouns_she,
            'pronounsHe': self.pronouns_he,
            'pronounsThey': self.pronouns_they,
            'pronounsCustom': self.pronouns_custom,

            'instagram': self.instagram,
            'twitter': self.twitter,
            'kofi': self.kofi,
            'website': self.website,

            'isSpinner': self.is_spinner,
            'isWeaver': self.is_weaver,
            'isKnitter': self.is_knitter,
            'isCrocheter': self.is_crocheter,
            'isSewist': self.is_sewist,
            'isEmbroiderer': self.is_embroiderer
        }
