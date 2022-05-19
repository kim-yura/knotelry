from multiprocessing import synchronize
from flask import Blueprint, jsonify, make_response, request
from flask_login import login_required
from app.models import db, User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/', methods=['PUT'])
def put_user():
    db.session.query(User).filter(User.id == request.json['id']).update({
        'bio': request.json['bio'],
        'crafting_journey': request.json['craftingJourney'],
        'roles': request.json['roles'],
        'profile_pic_url': request.json['profilePicURL'],
        'pronouns_she': request.json['pronounsShe'],
        'pronouns_he': request.json['pronounsHe'],
        'pronouns_they': request.json['pronounsThey'],
        'pronouns_custom': request.json['pronounsCustom'],
        'instagram': request.json['instagram'],
        'twitter': request.json['twitter'],
        'kofi': request.json['kofi'],
        'website': request.json['website'],
        'is_spinner': request.json['isSpinner'],
        'is_weaver': request.json['isWeaver'],
        'is_knitter': request.json['isKnitter'],
        'is_crocheter': request.json['isCrocheter'],
        'is_sewist': request.json['isSewist'],
        'is_embroiderer': request.json['isEmbroiderer'],
    }, synchronize_session='fetch')
    db.session.commit()
    user = User.query.get(request.json['id'])
    if user:
        return jsonify(user.to_dict())
    else: return make_response({ 'errors': ['Edit on non-existent user']}, 404)
