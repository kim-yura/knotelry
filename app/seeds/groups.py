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

    group3 = Group(
        id=3,
        title="Bloomington B's",
        description="A home for Bloomington crafters",
        country="US",
        owner_id=1,
    )
    group3_member1 = Group_Membership(
        group_id=3,
        user_id=1,
    )
    group3_member2 = Group_Membership(
        group_id=3,
        user_id=2,
    )
    group3_member3 = Group_Membership(
        group_id=3,
        user_id=3,
    )

    group4 = Group(
        id=4,
        title="Test Group 1",
        owner_id=1,
    )
    group4_member1 = Group_Membership(
        group_id=4,
        user_id=1,
    )

    group5 = Group(
        id=5,
        title="Test Group 2",
        owner_id=1,
    )
    group5_member1 = Group_Membership(
        group_id=5,
        user_id=1,
    )

    group6 = Group(
        id=6,
        title="Test Group 3",
        owner_id=1,
    )
    group6_member1 = Group_Membership(
        group_id=6,
        user_id=1,
    )

    group7 = Group(
        id=7,
        title="Test Group 4",
        owner_id=1,
    )
    group7_member1 = Group_Membership(
        group_id=7,
        user_id=1,
    )

    group8 = Group(
        id=8,
        title="Test Group 5",
        owner_id=1,
    )
    group8_member1 = Group_Membership(
        group_id=8,
        user_id=1,
    )

    db.session.add(group1)
    db.session.add(group1_member1)
    db.session.add(group1_member2)
    db.session.add(group1_member3)

    db.session.add(group2)
    db.session.add(group2_member1)
    db.session.add(group2_member2)

    db.session.add(group3)
    db.session.add(group3_member1)
    db.session.add(group3_member2)
    db.session.add(group3_member3)

    db.session.add(group4)
    db.session.add(group4_member1)

    db.session.add(group5)
    db.session.add(group5_member1)

    db.session.add(group6)
    db.session.add(group6_member1)

    db.session.add(group7)
    db.session.add(group7_member1)

    db.session.add(group8)
    db.session.add(group8_member1)

    db.session.commit()


def undo_groups():
    db.session.execute ('TRUNCATE group_memberships RESTART IDENTITY CASCADE;')
    db.session.execute ('TRUNCATE groups RESTART IDENTITY CASCADE;')
