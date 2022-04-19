from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import asc
from app.models import db, Gallery_Photo
from datetime import datetime

gallery_routes = Blueprint('gallery', __name__)



@gallery_routes.route('/users/<int:id>')
def get_users_photos(id):
    photos = Gallery_Photo.query.order_by((Gallery_Photo.id).asc()).all()
    usersPhotos = []
    for photo in photos:
        if photo.user_id == id:
            usersPhotos.append(photo)
    return {'photos': [photo.to_JSON() for photo in usersPhotos]}

@gallery_routes.route('/', methods=['POST'])
def post_photo():
    photo = Gallery_Photo(
        user_id = request.json['user_id'],
        image_url = request.json['image_url'],
        created_at = datetime.now()
    )
    try:
        db.session.add(photo)
        db.session.commit()
        return jsonify(photo.to_JSON())
    except:
        return make_response({f'errors': ['Error(s) on the gallery photo occurred']}, 400)

@gallery_routes.route('/', methods=['DELETE'])
def delete_photo():
    photo_id = request.json['id']
    photo = Gallery_Photo.query.get(photo_id)
    if photo:
        db.session.delete(photo)
        db.session.commit()
        return jsonify({'errors': False})
    else:
        return make_response({'errors': ['Delete on non-existent photo']}, 404)
