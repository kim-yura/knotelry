from datetime import datetime
from flask import Blueprint, jsonify, make_response, request
from app.models import db, Group, Group_Membership

group_routes = Blueprint('group', __name__)



@group_routes.route('/<int:id>')
def get_group(id):
    group = Group.query.get(id)
    return group.to_JSON()

@group_routes.route('/users/<int:id>')
def get_users_groups(id):
    groups = Group.query.all()

    return {'groups': [group for group in groups]}
