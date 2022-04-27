from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='DemoUser',
        email='demo@demo.com',
        password='demoPassword123',
        profile_pic_url='https://knotelry.s3.amazonaws.com/profilepic_1.jpg',
        bio='Just a crafty dev and SWE on the internet! Hire me to make cool sites like this for you.',
        crafting_journey="I started knitting in 2015 on a road trip with some friends. Since then, I've been hooked! I've expanded my repertoire from just knitting to also include designing knitwear, spinning, and dabbling in sewing and crocheting.",
        roles="knitwear designer, commmunity organizer, knotelry developer",
        pronouns_she=True,
        instagram='knitboop',
        twitter='knitwit_yura',
        kofi='knitboop',
        website='knitboop.com/',
        is_spinner=True,
        is_knitter=True,
        is_crocheter=True
    )
    knittywitty = User(
        username='knittywitty',
        email='knittywitty@email.com',
        password='password',
        is_spinner=True,
        is_knitter=True
    )
    purlsofwisdom = User(
        username='purlsofwisdom',
        email='purlsofwisdom@email.com',
        password='password',
        is_crocheter=True,
        is_sewist=True
    )
    stitchcraft = User(
        username='stitchcraft',
        email='stitchcraft@email.com',
        password='password'
    )

    db.session.add(demo)
    db.session.add(knittywitty)
    db.session.add(purlsofwisdom)
    db.session.add(stitchcraft)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
