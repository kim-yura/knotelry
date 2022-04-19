from app.models import db, Project, Project_Material, Project_Tool, Project_Image



def seed_projects():
    project1 = Project(
        user_id=1,
        title="Moose Hat",
        craft_types="knitting",

        pattern_name="Moose Camouflage Hat",
        pattern_author="Dawn Kinsey",
        link_to_pattern="https://www.ravelry.com/patterns/library/moose-camouflage-hat",

        tags="hat, accessory",
        status="finished",

        needle_sizes="2,3",

        attributes="in-the-round, colorwork",
        size_made="Large",
        description="Hat knit for Paul. He loves it!",
    )
    project1_material1 = Project_Material(
        project_id=1,
        stash_id=9,
        length_used=78.5,
        length_unit="yd",
        skeins_used=0.34,
    )
    project1_material2 = Project_Material(
        project_id=1,
        stash_id=10,
        length_used=55.4,
        length_unit="yd",
        skeins_used=0.24,
    )
    project1_material3 = Project_Material(
        project_id=1,
        stash_id=11,
        length_used=119,
        length_unit="yd",
        skeins_used=0.28,
    )
    project1_tool1 = Project_Tool(
        project_id=1,
        tool_id=3,
    )
    project1_image1 = Project_Image(
        project_id=1,
        image_url="https://knotelry.s3.amazonaws.com/project_1.jpg",
    )
    project1_image2 = Project_Image(
        project_id=1,
        image_url="https://knotelry.s3.amazonaws.com/project_2.jpg",
    )

    project2 = Project(
        user_id=1,
        title="Namu Sweater",
        craft_types="knitting",

        pattern_name="Namu Sweater",
        pattern_author="knitboop",
        link_to_pattern="https://www.knitboop.com/patterns/namu-sweater",

        tags="garment, sweater, pullover",
        status="finished",
        size_made='37" bust',
        attributes="cabled, in-the-round, top-down",
        stored_in="Handknit garment drawer",
        description="Sample for my first garment design, the Namu sweater. This is the second sample knit out of financially-accessible yarn options.",

        needle_sizes="6,7",
        gauge_count=16,
        gauge_unit="sts",
        gauge_rows=22,
        gauge_size_width=4,
        gauge_size_height=4,
        gauge_size_unit="in",
    )
    project2_material1 = Project_Material(
        project_id=2,
        stash_id=12,
        length_used=809.6,
        length_unit="yd",
        skeins_used=7.36,
    )
    project2_tool1 = Project_Tool(
        project_id=2,
        tool_id=3,
    )
    project2_image1 = Project_Image(
        project_id=2,
        image_url="https://knotelry.s3.amazonaws.com/project_3.jpg"
    )
    project2_image2 = Project_Image(
        project_id=2,
        image_url="https://knotelry.s3.amazonaws.com/project_4.jpg"
    )

    project3 = Project(
        user_id=1,
        title="Daybreak Socks",
        craft_types="knitting",

        pattern_name="Daybreak Socks",
        pattern_author="A Leong",

        tags="socks, accessory",
        status="finished",

        needle_sizes="1",
        description="Test knit for my friend A.",
    )
    project3_material1 = Project_Material(
        project_id=3,
        stash_id=13,
        length_used=252,
        length_unit="yd",
        skeins_used=0.63,
    )
    project3_tool1 = Project_Tool(
        project_id=3,
        tool_id=3,
    )
    project3_image1 = Project_Image(
        project_id=3,
        image_url="https://knotelry.s3.amazonaws.com/project_5.jpg"
    )
    project3_image2 = Project_Image(
        project_id=3,
        image_url="https://knotelry.s3.amazonaws.com/project_6.jpg"
    )
    project3_image3 = Project_Image(
        project_id=3,
        image_url="https://knotelry.s3.amazonaws.com/project_7.jpg"
    )

    project4 = Project(
        user_id=1,
        title="Spring in Brioche Cowl",
        craft_types="knitting",

        pattern_name="Spring in Brioche Cowl",
        pattern_author="Lavanya Patricella",
        link_to_pattern="https://www.etsy.com/listing/224309495/brioche-stitch-cowl-knitting-pdf-pattern?click_key=7e2089284c6ba7952837e7dceda255ce9a559418%3A224309495&click_sum=eab83553&ga_search_query=spring%2Bin%2Bbrioche&ref=shop_items_search_1",

        tags="cowl, accessory",
        status="finished",

        needle_sizes="6",
        description="Stash-busting Christmas gift project.",
    )
    project4_material1 = Project_Material(
        project_id=4,
        stash_id=14,
        length_used=216.1,
        length_unit="yd",
        skeins_used=1.46,
    )
    project4_material2 = Project_Material(
        project_id=4,
        stash_id=15,
        length_used=150,
        length_unit="yd",
        skeins_used=0.6,
    )
    project4_tool1 = Project_Tool(
        project_id=4,
        tool_id=3,
    )
    project4_image1 = Project_Image(
        project_id=4,
        image_url="https://knotelry.s3.amazonaws.com/project_8.jpg",
    )

    project5 = Project(
        user_id=1,
        title="Sugar Rush Handspun",
        craft_types="spinning",
        tags="handspinning",
        status="finished",
        attributes="top, semi-worsted, soaked, snapped, barber-pole, 2-ply",

        yarn_weight="lfingering",
        plies_count=2,
        twist_direction_singles="Z",
        twist_direction_plied="S",
    )
    project5_material1 = Project_Material(
        project_id=5,
        stash_id=2,
        fiber_quantity_used=4,
        fiber_quantity_unit="oz"
    )
    project5_material2 = Project_Material(
        project_id=5,
        stash_id=3,
        fiber_quantity_used=4,
        fiber_quantity_unit="oz"
    )
    project5_tool1 = Project_Tool(
        project_id=5,
        tool_id=1,
    )
    project5_image1 = Project_Image(
        project_id=5,
        image_url="https://knotelry.s3.amazonaws.com/project_9.jpg",
    )
    project5_image2 = Project_Image(
        project_id=5,
        image_url="https://knotelry.s3.amazonaws.com/project_10.jpg",
    )

    project6 = Project(
        user_id=1,
        title="Koomasee Fiber Spin",
        craft_types="spinning",
        tags="handspinning",
        status="finished",
        attributes="top, semi-worsted, soaked, snapped, barber-pole, 2-ply",

        yarn_weight="lfingering",
        plies_count=2,
        twist_direction_singles="Z",
        twist_direction_plied="S",
    )
    project6_material1 = Project_Material(
        project_id=6,
        stash_id=16,
        fiber_quantity_used=4,
        fiber_quantity_unit="oz",
    )
    project6_material2 = Project_Material(
        project_id=6,
        stash_id=17,
        fiber_quantity_used=4,
        fiber_quantity_unit="oz",
    )
    project6_tool1 = Project_Tool(
        project_id=6,
        tool_id=1,
    )
    project6_image1 = Project_Image(
        project_id=6,
        image_url="https://knotelry.s3.amazonaws.com/project_11.jpg",
    )
    project6_image2 = Project_Image(
        project_id=6,
        image_url="https://knotelry.s3.amazonaws.com/project_12.jpg",
    )
    project6_image3 = Project_Image(
        project_id=6,
        image_url="https://knotelry.s3.amazonaws.com/project_13.jpg",
    )

    db.session.add(project1)
    db.session.add(project1_material1)
    db.session.add(project1_material2)
    db.session.add(project1_material3)
    db.session.add(project1_tool1)
    db.session.add(project1_image1)
    db.session.add(project1_image2)

    db.session.add(project2)
    db.session.add(project2_material1)
    db.session.add(project2_tool1)
    db.session.add(project2_image1)
    db.session.add(project2_image2)

    db.session.add(project3)
    db.session.add(project3_material1)
    db.session.add(project3_tool1)
    db.session.add(project3_image1)
    db.session.add(project3_image2)
    db.session.add(project3_image3)

    db.session.add(project4)
    db.session.add(project4_material1)
    db.session.add(project4_material2)
    db.session.add(project4_tool1)
    db.session.add(project4_image1)

    db.session.add(project5)
    db.session.add(project5_material1)
    db.session.add(project5_material2)
    db.session.add(project5_tool1)
    db.session.add(project5_image1)
    db.session.add(project5_image2)

    db.session.add(project6)
    db.session.add(project6_material1)
    db.session.add(project6_material2)
    db.session.add(project6_tool1)
    db.session.add(project6_image1)
    db.session.add(project6_image2)
    db.session.add(project6_image3)

    db.session.commit()


def undo_projects():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE project_materials RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE project_tools RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE project_images RESTART IDENTITY CASCADE;')
