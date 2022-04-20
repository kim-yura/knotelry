from datetime import datetime
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import asc
from app.models import db, Stash_Item, Stash_Item_Image, Project, Project_Material

stash_routes = Blueprint('stash', __name__)



@stash_routes.route('/users/<int:id>')
def get_users_stash(id):
    stash = Stash_Item.query.order_by((Stash_Item.id).asc()).all()
    users_stash = []
    for stash_item in stash:
        if stash_item.user_id == id:
            users_stash.append(stash_item)
    return {'stash': [stash_item.to_JSON() for stash_item in users_stash]}

@stash_routes.route('/<int:id>')
def stash_item(id):
    stash_item = Stash_Item.query.get(id)
    return stash_item.to_JSON()

@stash_routes.route('/<int:id>/images')
def get_linked_images(id):
    stash_item_images = Stash_Item_Image.query.order_by((Stash_Item_Image.id).asc()).all()
    linked_images = []
    for image in stash_item_images:
        if image.stash_item_id == id:
            linked_images.append(image)
    return {'linkedImages': [image.to_JSON() for image in linked_images]}

@stash_routes.route('/<int:id>/projects')
def get_linked_projects(id):
    project_materials = Project_Material.query.order_by((Project_Material.project_id).asc()).all()
    linked_project_materials = []
    for material in project_materials:
        if material.stash_id == id:
            linked_project_materials.append(material)
    linked_projects = []
    for material in linked_project_materials:
        project = Project.query.get(material.project_id)
        linked_projects.append(project)
    return {'linkedProjects': [project.to_JSON() for project in linked_projects]}

@stash_routes.route('/<int:id>/projectmaterials')
def get_linked_project_materials(id):
    project_materials = Project_Material.query.order_by((Project_Material.project_id).asc()).all()
    linked_project_materials = []
    for material in project_materials:
        if material.stash_id == id:
            linked_project_materials.append(material)
    return {'linkedProjectMaterials': [material.to_JSON() for material in linked_project_materials]}

@stash_routes.route('/', methods=['POST'])
def post_stash_item():
    stash_item = Stash_Item(
        user_id = request.json['user_id'],

        title = request.json['title'],
        description = request.json['description'],
        type = request.json['type'],

        status = request.json['status'],
        tags = request.json['tags'],
        attributes = request.json['attributes'],
        stored_in = request.json['stored_in'],

        acquired = request.json['acquired'],
        acquired_from = request.json['acquired_from'],
        acquired_price = request.json['acquired_price'],
        acquired_currency = request.json['acquired_currency'],

        colors = request.json['colors'],

        dyer_name = request.json['dyer_name'],
        colorway_name = request.json['colorway_name'],
        fiber_content = request.json['fiber_content'],

        fiber_quantity = request.json['fiber_quantity'],
        fiber_quantity_unit = request.json['fiber_quantity_unit'],

        yarn_weight = request.json['yarn_weight'],
        length_per_skein = request.json['length_per_skein'],
        length_unit = request.json['length_unit'],
        weight_per_skein = request.json['weight_per_skein'],
        weight_unit = request.json['weight_unit'],
        skeins_stashed = request.json['skeins_stashed'],
        length_stashed = request.json['length_stashed'],
        weight_stashed = request.json['weight_stashed'],
        is_handspun = request.json['is_handspun'],

        fabric_width = request.json['fabric_width'],
        fabric_width_unit = request.json['fabric_width_unit'],
        fabric_weight = request.json['fabric_weight'],
        fabric_weight_unit = request.json['fabric_weight_unit'],
        fabric_weight_area_unit = request.json['fabric_weight_area_unit'],
        fabric_pattern_repeat_width = request.json['fabric_pattern_repeat_width'],
        fabric_pattern_repeat_height = request.json['fabric_pattern_repeat_height'],
        fabric_pattern_repeat_unit = request.json['fabric_pattern_repeat_unit'],

        notes = request.json['notes'],
        created_at = datetime.now(),
        updated_at = datetime.now(),
    )
    try:
        db.session.add(stash_item)
        db.session.commit()
        return jsonify(stash_item.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the stash item occurred']}, 400)

@stash_routes.route('/images/', methods=['POST'])
def post_stash_item_image():
    stash_item_image = Stash_Item_Image(
        stash_item_id = request.json['stash_item_id'],
        image_url = request.json['image_url'],
    )
    try:
        db.session.add(stash_item_image)
        db.session.commit()
        return jsonify(stash_item_image.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the stash item image occurred']}, 400)

@stash_routes.route('/', methods=['PUT'])
def put_stash_item():
    db.session.query(Stash_Item).filter(Stash_Item.id == request.json['id']).update({
        'title': request.json['title'],
        'description': request.json['description'],
        'type': request.json['type'],

        'status': request.json['status'],
        'tags': request.json['tags'],
        'attributes': request.json['attributes'],
        'stored_in': request.json['stored_in'],

        'acquired': request.json['acquired'],
        'acquired_from': request.json['acquired_from'],
        'acquired_price': request.json['acquired_price'],
        'acquired_currency': request.json['acquired_currency'],

        'colors': request.json['colors'],

        'dyer_name': request.json['dyer_name'],
        'colorway_name': request.json['colorway_name'],
        'fiber_content': request.json['fiber_content'],

        'fiber_quantity': request.json['fiber_quantity'],
        'fiber_quantity_unit': request.json['fiber_quantity_unit'],

        'yarn_weight': request.json['yarn_weight'],
        'length_per_skein': request.json['length_per_skein'],
        'length_unit': request.json['length_unit'],
        'weight_per_skein': request.json['weight_per_skein'],
        'weight_unit': request.json['weight_unit'],
        'skeins_stashed': request.json['skeins_stashed'],
        'length_stashed': request.json['length_stashed'],
        'weight_stashed': request.json['weight_stashed'],
        'is_handspun': request.json['is_handspun'],

        'fabric_width': request.json['fabric_width'],
        'fabric_width_unit': request.json['fabric_width_unit'],
        'fabric_weight': request.json['fabric_weight'],
        'fabric_weight_unit': request.json['fabric_weight_unit'],
        'fabric_weight_area_unit': request.json['fabric_weight_area_unit'],
        'fabric_pattern_repeat_width': request.json['fabric_pattern_repeat_width'],
        'fabric_pattern_repeat_height': request.json['fabric_pattern_repeat_height'],
        'fabric_pattern_repeat_unit': request.json['fabric_pattern_repeat_unit'],

        'notes': request.json['notes'],
        'updated_at': datetime.now(),
    }, synchronize_session='fetch')
    db.session.commit()
    stash_item = Stash_Item.query.get(request.json['id'])
    if stash_item:
        return jsonify(stash_item.to_JSON())
    else:
        return make_response({'errors': ['Edit on non-existent stash item']}, 404)

@stash_routes.route('/', methods=['DELETE'])
def delete_stash_item():
    stash_item_id = request.json['id']
    stash_item = Stash_Item.query.get(stash_item_id)
    if stash_item:
        db.session.delete(stash_item)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent stash item']}, 404)

@stash_routes.route('/images/', methods=['DELETE'])
def delete_stash_item_image():
    stash_item_image = Stash_Item_Image.query.get(request.json['id'])
    if stash_item_image:
        db.session.delete(stash_item_image)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent stash item image']}, 404)
