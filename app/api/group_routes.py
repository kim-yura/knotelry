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
    group_memberships = Group_Membership.query.all()
    users_memberships = []
    for membership in group_memberships:
        if membership.user_id == id:
            users_memberships.append(membership)
    users_groups = []
    for membership in users_memberships:
        users_groups.append(Group.query.get(membership.group_id))

    return {'usersGroups': [group.to_JSON() for group in users_groups]}
