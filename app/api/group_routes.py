from datetime import datetime
from flask import Blueprint, jsonify, make_response, request
from app.models import db, Group, Group_Membership, User

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

@group_routes.route('/<int:id>/members')
def get_groups_members(id):
    group_memberships = Group_Membership.query.all()
    group_members = []
    for membership in group_memberships:
        if membership.group_id == id:
            group_members.append(User.query.get(membership.user_id))
    return {'groupMembers': [member.to_JSON() for member in group_members]}

@group_routes.route('/', methods=['POST'])
def post_group():
    group = Group(
        title = request.json['title'],
        description = request.json['description'],
        craft_types = request.json['craft_types'],
        country = request.json['country'],
        owner_id = request.json['owner_id'],
        moderator_ids = request.json['moderator_ids'],
        created_at = datetime.now(),
    )
    try:
        db.session.add(group)
        db.session.commit()
        return jsonify(group.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the group occurred']}, 400)

@group_routes.route('/<int:id>/join', methods=['POST'])
def join_group(id):
    group_membership = Group_Membership(
        group_id = id,
        user_id = request.json['user_id'],
        created_at = datetime.now(),
    )
    try:
        db.session.add(group_membership)
        db.session.commit()
        return jsonify(group_membership.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the group membership occurred']}, 400)

@group_routes.route('/', methods=['PUT'])
def put_group():
    db.session.query(Group).filter(Group.id == request.json['id']).update({
        'title': request.json['title'],
        'description': request.json['description'],
        'craft_types': request.json['craft_types'],
        'country': request.json['country'],
        'moderator_ids': request.json['moderator_ids'],
    }, synchronize_session='fetch')
    db.session.commit()
    group = Group.query.get(request.json['id'])
    if group:
        return jsonify(group.to_JSON())
    else:
        return make_response({'errors': ['Edit on non-existent group']}, 404)
