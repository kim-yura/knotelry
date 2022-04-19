from datetime import datetime
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import asc
from app.models import db, Tool

tool_routes = Blueprint('tools', __name__)


@tool_routes.route('/users/<int:id>')
def get_users_tools(id):
    tools = Tool.query.order_by((Tool.id).asc()).all()
    usersTools = []
    for tool in tools:
        if tool.user_id == id:
            usersTools.append(tool)
    return {'tools': [tool.to_JSON() for tool in usersTools]}

@tool_routes.route('/<int:id>')
def tool(id):
    tool = Tool.query.get(id)
    return tool.to_JSON()

@tool_routes.route('/', methods=['POST'])
def post_tool():
    tool = Tool(
        user_id = request.json['user_id'],
        title = request.json['title'],
        description = request.json['description'],
        acquired = request.json['acquired'],
        status = request.json['status'],
        created_at = datetime.now(),
        updated_at = datetime.now(),

        for_spinning = request.json['for_spinning'],
        for_weaving = request.json['for_weaving'],
        for_knitting = request.json['for_knitting'],
        for_crocheting = request.json['for_crocheting'],
        for_sewing = request.json['for_sewing'],
        for_embroidery = request.json['for_embroidery'],

        image_url = request.json['image_url'],
    )
    try:
        db.session.add(tool)
        db.session.commit()
        return jsonify(tool.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the tool occurred']}, 400)

@tool_routes.route('/', methods=['PUT'])
def put_tool():
    db.session.query(Tool).filter(Tool.id == request.json['id']).update({
        'title': request.json['title'],
        'description': request.json['description'],
        'acquired': request.json['acquired'],
        'status': request.json['status'],
        'updated_at': datetime.now(),

        'for_spinning': request.json['for_spinning'],
        'for_weaving': request.json['for_weaving'],
        'for_knitting': request.json['for_knitting'],
        'for_crocheting': request.json['for_crocheting'],
        'for_sewing': request.json['for_sewing'],
        'for_embroidery': request.json['for_embroidery'],

        'image_url': request.json['image_url'],

    }, synchronize_session='fetch')
    db.session.commit()
    tool = Tool.query.get(request.json['id'])
    if tool:
        return jsonify(tool.to_JSON())
    else:
        return make_response({'errors': ['Edit on non-existent tool']}, 404)

@tool_routes.route('/favorite', methods=['PUT'])
def favorite_tool():
    db.session.query(Tool).filter(Tool.id == request.json['id']).update({
        'favorited': True,
        'updated_at': datetime.now(),
    }, synchronize_session='fetch')
    db.session.commit()
    tool = Tool.query.get(request.json['id'])
    if tool:
        return jsonify(tool.to_JSON())
    else:
        return make_response({'errors': ['Favorite on non-existent tool']}, 404)

@tool_routes.route('/unfavorite', methods=['PUT'])
def unfavorite_tool():
    db.session.query(Tool).filter(Tool.id == request.json['id']).update({
        'favorited': False,
        'updated_at': datetime.now(),
    }, synchronize_session='fetch')
    db.session.commit()
    tool = Tool.query.get(request.json['id'])
    if tool:
        return jsonify(tool.to_JSON())
    else:
        return make_response({'errors': ['Unfavorite on non-existent tool']}, 404)

@tool_routes.route('/', methods=['DELETE'])
def delete_tool():
    tool_id = request.json['id']
    tool = Tool.query.get(tool_id)
    if tool:
        db.session.delete(tool)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent scrap']}, 404)
