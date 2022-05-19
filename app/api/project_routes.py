from datetime import datetime
from flask import Blueprint, jsonify, make_response, request
from app.models import db, Project, Project_Material, Project_Tool, Project_Image

project_routes = Blueprint('project', __name__)



@project_routes.route('/users/<int:id>')
def get_users_projects(id):
    projects = Project.query.order_by((Project.id).asc()).all()
    users_projects = []
    for project in projects:
        if project.user_id == id:
            users_projects.append(project)
    return {'projects': [project.to_JSON() for project in users_projects]}

@project_routes.route('/<int:id>')
def get_project(id):
    project = Project.query.get(id)
    return project.to_JSON()

@project_routes.route('/<int:id>/materials')
def get_linked_materials(id):
    project_materials = Project_Material.query.order_by((Project_Material.id).asc()).all()
    linked_materials = []
    for material in project_materials:
        if material.project_id == id:
            linked_materials.append(material)
    return {'linkedMaterials': [material.to_JSON() for material in linked_materials]}

@project_routes.route('/<int:id>/tools')
def get_linked_tools(id):
    project_tools = Project_Tool.query.order_by((Project_Tool.project_id).asc()).all()
    linked_tools = []
    for tool in project_tools:
        if tool.project_id == id:
            linked_tools.append(tool)
    return {'linkedTools': [tool.to_JSON() for tool in linked_tools]}

@project_routes.route('/<int:id>/images')
def get_linked_images(id):
    project_images = Project_Image.query.order_by((Project_Image.project_id).asc()).all()
    linked_images = []
    for image in project_images:
        if image.project_id == id:
            linked_images.append(image)
    return {'linkedImages': [image.to_JSON() for image in linked_images]}

@project_routes.route('/', methods=['POST'])
def post_project():
    project = Project(
        user_id = request.json['user_id'],
        title = request.json['title'],
        description = request.json['description'],
        craft_types = request.json['craft_types'],
        pattern_name = request.json['pattern_name'],
        pattern_author = request.json['pattern_author'],
        link_to_pattern = request.json['link_to_pattern'],
        size_made = request.json['size_made'],
        tags = request.json['tags'],
        status = request.json['status'],
        attributes = request.json['attributes'],
        stored_in = request.json['stored_in'],
        start_date = request.json['start_date'],
        end_date = request.json['end_date'],

        # Spinning
        yarn_weight = request.json['yarn_weight'],
        grist = request.json['grist'],
        grist_unit = request.json['grist_unit'],
        wpi = request.json['wpi'],
        plies_count = request.json['plies_count'],
        twist_direction_singles = request.json['twist_direction_singles'],
        twist_direction_plied = request.json['twist_direction_plied'],
        twist_angle = request.json['twist_angle'],
        drive_ratio_singles = request.json['drive_ratio_singles'],
        drive_ratio_plied = request.json['drive_ratio_plied'],
        finished_yarn_length = request.json['finished_yarn_length'],
        finished_yarn_length_unit = request.json['finished_yarn_length_unit'],
        finished_yarn_weight = request.json['finished_yarn_weight'],
        finished_yarn_weight_unit = request.json['finished_yarn_weight_unit'],

        # Weaving
        warp_yarn = request.json['warp_yarn'],
        weft_yarn = request.json['weft_yarn'],
        epi = request.json['epi'],
        ppi = request.json['ppi'],
        total_ends = request.json['total_ends'],
        draft_notes = request.json['draft_notes'],

        width_in_reed = request.json['width_in_reed'],
        width_in_reed_unit = request.json['width_in_reed_unit'],
        warped_length = request.json['warped_length'],
        warped_length_unit = request.json['warped_length_unit'],
        length = request.json['length'],
        length_unit = request.json['length_unit'],
        finished_length = request.json['finished_length'],
        finished_length_unit = request.json['finished_length_unit'],
        finished_width = request.json['finished_width'],
        finished_width_unit = request.json['finished_width_unit'],

        # Knitting
        needle_sizes = request.json['needle_sizes'],
        knit_gauge_count = request.json['knit_gauge_count'],
        knit_gauge_unit = request.json['knit_gauge_unit'],
        knit_gauge_rows = request.json['knit_gauge_rows'],
        knit_gauge_size_width = request.json['knit_gauge_size_width'],
        knit_gauge_size_height = request.json['knit_gauge_size_height'],
        knit_gauge_size_unit = request.json['knit_gauge_size_unit'],

        # Crocheting
        hook_sizes = request.json['hook_sizes'],
        crochet_gauge_count = request.json['crochet_gauge_count'],
        crochet_gauge_unit = request.json['crochet_gauge_unit'],
        crochet_gauge_rows = request.json['crochet_gauge_rows'],
        crochet_gauge_size_width = request.json['crochet_gauge_size_width'],
        crochet_gauge_size_height = request.json['crochet_gauge_size_height'],
        crochet_gauge_size_unit = request.json['crochet_gauge_size_unit'],

        notes = request.json['notes'],
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    try:
        db.session.add(project)
        db.session.commit()
        return jsonify(project.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the project occurred']}, 400)

@project_routes.route('/materials/', methods=['POST'])
def post_project_material():
    project_material = Project_Material(
        project_id = request.json['project_id'],
        stash_id = request.json['stash_id'],

        fiber_quantity_used = request.json['fiber_quantity_used'],
        fiber_quantity_unit = request.json['fiber_quantity_unit'],
        length_used = request.json['length_used'],
        length_unit = request.json['length_unit'],
        weight_used = request.json['weight_used'],
        weight_unit = request.json['weight_unit'],
        skeins_used = request.json['skeins_used'],
        units_used = request.json['units_used'],
    )
    try:
        db.session.add(project_material)
        db.session.commit()
        return jsonify(project_material.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the project material occurred']}, 400)

@project_routes.route('/tools/', methods=['POST'])
def post_project_tool():
    project_tool = Project_Tool(
        project_id = request.json['project_id'],
        tool_id = request.json['tool_id'],
    )
    try:
        db.session.add(project_tool)
        db.session.commit()
        return jsonify(project_tool.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the project tool occurred']}, 400)

@project_routes.route('/images/', methods=['POST'])
def post_project_image():
    project_image = Project_Image(
        project_id = request.json['project_id'],
        image_url = request.json['image_url'],
    )
    try:
        db.session.add(project_image)
        db.session.commit()
        return jsonify(project_image.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the project image occurred']}, 400)

@project_routes.route('/', methods=['PUT'])
def put_project():
    db.session.query(Project).filter(Project.id == request.json['id']).update({
        'title': request.json['title'],
        'description': request.json['description'],
        'craft_types': request.json['craft_types'],
        'pattern_name': request.json['pattern_name'],
        'pattern_author': request.json['pattern_author'],
        'link_to_pattern': request.json['link_to_pattern'],
        'size_made': request.json['size_made'],
        'tags': request.json['tags'],
        'status': request.json['status'],
        'attributes': request.json['attributes'],
        'stored_in': request.json['stored_in'],
        'start_date': request.json['start_date'],
        'end_date': request.json['end_date'],

        'yarn_weight': request.json['yarn_weight'],
        'grist': request.json['grist'],
        'grist_unit': request.json['grist_unit'],
        'wpi': request.json['wpi'],
        'plies_count': request.json['plies_count'],
        'twist_direction_singles': request.json['twist_direction_singles'],
        'twist_direction_plied': request.json['twist_direction_plied'],
        'twist_angle': request.json['twist_angle'],
        'drive_ratio_singles': request.json['drive_ratio_singles'],
        'drive_ratio_plied': request.json['drive_ratio_plied'],
        'finished_yarn_length': request.json['finished_yarn_length'],
        'finished_yarn_length_unit': request.json['finished_yarn_length_unit'],
        'finished_yarn_weight': request.json['finished_yarn_weight'],
        'finished_yarn_weight_unit': request.json['finished_yarn_weight_unit'],

        'warp_yarn': request.json['warp_yarn'],
        'weft_yarn': request.json['weft_yarn'],
        'epi': request.json['epi'],
        'ppi': request.json['ppi'],
        'total_ends': request.json['total_ends'],
        'draft_notes': request.json['draft_notes'],

        'width_in_reed': request.json['width_in_reed'],
        'width_in_reed_unit': request.json['width_in_reed_unit'],
        'warped_length': request.json['warped_length'],
        'warped_length_unit': request.json['warped_length_unit'],
        'length': request.json['length'],
        'length_unit': request.json['length_unit'],
        'finished_length': request.json['finished_length'],
        'finished_length_unit': request.json['finished_length_unit'],
        'finished_width': request.json['finished_width'],
        'finished_width_unit': request.json['finished_width_unit'],

        'needle_sizes': request.json['needle_sizes'],
        'knit_gauge_count': request.json['knit_gauge_count'],
        'knit_gauge_unit': request.json['knit_gauge_unit'],
        'knit_gauge_rows': request.json['knit_gauge_rows'],
        'knit_gauge_size_width': request.json['knit_gauge_size_width'],
        'knit_gauge_size_height': request.json['knit_gauge_size_height'],
        'knit_gauge_size_unit': request.json['knit_gauge_size_unit'],

        'hook_sizes': request.json['hook_sizes'],
        'crochet_gauge_count': request.json['crochet_gauge_count'],
        'crochet_gauge_unit': request.json['crochet_gauge_unit'],
        'crochet_gauge_rows': request.json['crochet_gauge_rows'],
        'crochet_gauge_size_width': request.json['crochet_gauge_size_width'],
        'crochet_gauge_size_height': request.json['crochet_gauge_size_height'],
        'crochet_gauge_size_unit': request.json['crochet_gauge_size_unit'],

        'notes': request.json['notes'],
        'updated_at': datetime.now(),
    }, synchronize_session='fetch')
    db.session.commit()
    project = Project.query.get(request.json['id'])
    if project:
        return jsonify(project.to_JSON())
    else:
        return make_response({'errors': ['Edit on non-existent project']}, 404)

@project_routes.route('/materials/', methods=['PUT'])
def put_project_material():
    db.session.query(Project_Material).filter(Project_Material.id == request.json['id']).update({
        'fiber_quantity_used': request.json['fiber_quantity_used'],
        'fiber_quantity_unit': request.json['fiber_quantity_unit'],
        'length_used': request.json['length_used'],
        'length_unit': request.json['length_unit'],
        'weight_used': request.json['weight_used'],
        'weight_unit': request.json['weight_unit'],
        'skeins_used': request.json['skeins_used'],
        'units_used': request.json['units_used'],
    }, synchronize_session='fetch')
    db.session.commit()
    project_material = Project_Material.query.get(request.json['id'])
    if project_material:
        return jsonify(project_material.to_JSON())
    else:
        return make_response({'errors': ['Edit on non-existent project material']}, 404)

@project_routes.route('/', methods=['DELETE'])
def delete_project():
    project = Project.query.get(request.json['id'])
    if project:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent project']}, 404)

@project_routes.route('/materials/', methods=['DELETE'])
def delete_project_material():
    project_material = Project_Material.query.get(request.json['id'])
    if project_material:
        db.session.delete(project_material)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent project material']}, 404)

@project_routes.route('/tools/', methods=['DELETE'])
def delete_project_tool():
    project_tool = Project_Tool.query.get(request.json['id'])
    if project_tool:
        db.session.delete(project_tool)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent project tool']}, 404)

@project_routes.route('/images/', methods=['DELETE'])
def delete_project_image():
    project_image = Project_Image.query.get(request.json['id'])
    if project_image:
        db.session.delete(project_image)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent project image']}, 404)
