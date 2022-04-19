from app.models import db, Tool
from datetime import datetime


def seed_tools():
    tool1 = Tool(
        user_id=1,
        title='Electric Eel Wheel 6',
        description='EEW 6.0 from Kickstarter campaign',
        acquired=datetime(2021, 4, 1),
        status='inUse',
        favorited=True,
        for_spinning=True,
        image_url="https://knotelry.s3.amazonaws.com/tool1_img.jpg"
    )
    tool2 = Tool(
        user_id=1,
        title='Ashford Rigid Heddle Loom',
        description='Loaned out to fiber guild member Linda',
        status='loaned',
        for_weaving=True
    )
    tool3 = Tool(
        user_id=1,
        title='ChiaoGoo Interchangeables Set with 5" Tips',
        status='inStash',
        favorited=True,
        for_knitting=True
    )
    tool4 = Tool(
        user_id=1,
        title='Furls Candy Shop Crochet Hooks set',
        status='inStash',
        favorited=True,
        for_crocheting=True,
        image_url="https://knotelry.s3.amazonaws.com/tool4_img.jpg"
    )
    tool5 = Tool(
        user_id=1,
        title='Antique Singer Sewing Machine',
        status='inUse',
        favorited=True,
        for_sewing=True
    )
    tool6 = Tool(
        user_id=1,
        title='Magnetic Needle Minder',
        status='inStash',
        for_embroidery=True,
        image_url="https://knotelry.s3.amazonaws.com/tool6_img.jpg"
    )
    tool7 = Tool(
        user_id=2,
        title='Test tool that should not show up for DemoUser',
    )

    db.session.add(tool1)
    db.session.add(tool2)
    db.session.add(tool3)
    db.session.add(tool4)
    db.session.add(tool5)
    db.session.add(tool6)
    db.session.add(tool7)

    db.session.commit()



def undo_tools():
    db.session.execute('TRUNCATE tools RESTART IDENTITY CASCADE;')
    db.session.commit()
