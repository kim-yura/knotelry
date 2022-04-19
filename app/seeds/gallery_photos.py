from app.models import db, Gallery_Photo
from datetime import datetime


def seed_gallery_photos():
    photo1 = Gallery_Photo(
        user_id=1,
        image_url='https://knotelry.s3.amazonaws.com/gallery_1.jpg',
    )
    photo2 = Gallery_Photo(
        user_id=1,
        image_url='https://knotelry.s3.amazonaws.com/gallery_2.jpg',
    )
    photo3 = Gallery_Photo(
        user_id=1,
        image_url='https://knotelry.s3.amazonaws.com/gallery_3.jpg',
    )
    photo4 = Gallery_Photo(
        user_id=1,
        image_url='https://knotelry.s3.amazonaws.com/gallery_4.jpg'
    )

    db.session.add(photo1)
    db.session.add(photo2)
    db.session.add(photo3)
    db.session.add(photo4)

    db.session.commit()


def undo_gallery_photos():
    db.session.execute('TRUNCATE gallery_photos RESTART IDENTITY CASCADE;')
    db.session.commit()
