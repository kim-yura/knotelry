from app.models import db, Group, Group_Membership
from datetime import datetime


def seed_groups():
    group1 = Group(
        id=1,
        title="knotelry Dev Announcements",
        description="The forum group for any and all knotelry updates!",
        country="US",
        owner_id=1,
        moderator_ids="2",
    )
    group1_member1 = Group_Membership(
        group_id=1,
        user_id=1,
    )
    group1_member2 = Group_Membership(
        group_id=1,
        user_id=2,
    )
    group1_member3 = Group_Membership(
        group_id=1,
        user_id=3,
    )

    group2 = Group(
        id=2,
        title="Test Group Without Knitboop",
        description="A group without knitboop :(",
        country="AQ",
        owner_id=2,
        moderator_ids="3",
    )
    group2_member1 = Group_Membership(
        group_id=2,
        user_id=2,
    )
    group2_member2 = Group_Membership(
        group_id=2,
        user_id=3,
    )

    db.session.add(group1)
    db.session.add(group1_member1)
    db.session.add(group1_member2)
    db.session.add(group1_member3)

    db.session.add(group2)
    db.session.add(group2_member1)
    db.session.add(group2_member2)

    db.session.commit()


def undo_groups():
    db.session.execute ('TRUNCATE group_memberships RESTART IDENTITY CASCADE;')
    db.session.execute ('TRUNCATE groups RESTART IDENTITY CASCADE;')
