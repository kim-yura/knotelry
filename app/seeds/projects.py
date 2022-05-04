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
        knit_gauge_count=16,
        knit_gauge_unit="sts",
        knit_gauge_rows=22,
        knit_gauge_size_width=4,
        knit_gauge_size_height=4,
        knit_gauge_size_unit="in",
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

        finished_yarn_length=938,
        finished_yarn_length_unit="yd",
        finished_yarn_weight=202,
        finished_yarn_weight_unit="g",
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

        finished_yarn_length=620,
        finished_yarn_length_unit="yd",
        finished_yarn_weight=269,
        finished_yarn_weight_unit="g",
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

    project7 = Project(
        user_id=1,
        title="Small Project Bag 1",
        craft_types="sewing",
        status="finished",
    )
    project7_material1 = Project_Material(
        project_id=7,
        stash_id=25,
        length_used=2,
        length_unit="yd",
    )
    project7_image1 = Project_Image(
        project_id=7,
        image_url="https://knotelry.s3.amazonaws.com/project_14.jpg"
    )
    project7_image2 = Project_Image(
        project_id=7,
        image_url="https://knotelry.s3.amazonaws.com/project_15.jpg"
    )

    project8 = Project(
        user_id=1,
        title="Small Project Bag 2",
        craft_types="sewing",
        status="finished",
    )
    project8_material1 = Project_Material(
        project_id=8,
        stash_id=26,
        length_used=2,
        length_unit="yd",
    )
    project8_image1 = Project_Image(
        project_id=8,
        image_url="https://knotelry.s3.amazonaws.com/project_16.jpg"
    )
    project8_image2 = Project_Image(
        project_id=8,
        image_url="https://knotelry.s3.amazonaws.com/project_17.jpg"
    )
    project8_image3 = Project_Image(
        project_id=8,
        image_url="https://knotelry.s3.amazonaws.com/project_18.jpg"
    )

    project9 = Project(
        user_id=1,
        title="Smitten Scarf",
        craft_types="weaving",
        warp_yarn="Handmaiden Fine Yarn Smitten",
        weft_yarn="Handmaiden Fine Yarn Smitten",
        epi=7.5,
        ppi=7.5,
        draft_notes="Just a plain weave scarf.",

        warped_length=84,
        warped_length_unit="in",
        finished_length=66,
        finished_length_unit="in",
        finished_width=6.5,
        finished_width_unit="in",

        notes='Just a plain weave scarf. Very stretchy (and very beautiful) knitting yarn. Warped 84”. Alternated hot/cold baths, thrown in the dryer on high heat, then steam pressed. Final scarf measurements: 6.5” wide, 66” long (excluding 2” fringe each end).',
    )
    project9_image1 = Project_Image(
        project_id=9,
        image_url="https://knotelry.s3.amazonaws.com/project_19.jpg",
    )
    project9_image2 = Project_Image(
        project_id=9,
        image_url="https://knotelry.s3.amazonaws.com/project_20.jpg",
    )

    project10 = Project(
        user_id=1,
        title="Scrap Towels",
        craft_types="weaving",
        epi=20,
        ppi=20,
        total_ends=400,
        draft_notes="2/2 twill biased",

        width_in_reed=20,
        width_in_reed_unit="in",
        warped_length=4.5,
        warped_length_unit="yd",
        finished_length=25,
        finished_length_unit="in",
        finished_width=16.5,
        finished_width_unit="in",

        notes='I was able to get 4 towels and a little sampler. Final measurements after hemming, washing, drying and pressing: 16.5” by 25”. They are a little wonky. The 2/2 twill biased and you can see how the natural cottolin behaves differently from the dyed cottolin. But they are very soft and thirsty. Maybe a little too long.',
    )
    project10_image1 = Project_Image(
        project_id=10,
        image_url="https://knotelry.s3.amazonaws.com/project_21.jpg",
    )
    project10_image2 = Project_Image(
        project_id=10,
        image_url="https://knotelry.s3.amazonaws.com/project_22.jpg"
    )
    project10_image3 = Project_Image(
        project_id=10,
        image_url="https://knotelry.s3.amazonaws.com/project_23.jpg"
    )
    project10_image4 = Project_Image(
        project_id=10,
        image_url="https://knotelry.s3.amazonaws.com/project_24.jpg"
    )

    project11 = Project(
        user_id=1,
        title="Dash Scarf",
        craft_types="weaving",
        warp_yarn="Northbound Knitting Cotton Lace",
        weft_yarn="Northbound Knitting Cotton Lace",
        epi=24,
        draft_notes="Weaving pattern by Amanda Rataj, available here: https://amandarataj.com/index.php/product/dash-tea-towels-pdf-pattern/",

        length=81,
        length_unit="in",
        width_in_reed=20,
        width_in_reed_unit="in",
        warped_length=3,
        warped_length_unit="yd",
        finished_length=73,
        finished_length_unit="in",
        finished_width=18.5,
        finished_width_unit="in",

        notes="This handdyed cotton yarn seems the equivalent of 10/2 cotton, and I’ll be making a scarf, rather than tea towels.Aquarius, Sterling, Pacific, Seafoam, Denim, Wheat, Conch, Papyrus, Copper. Modified the draft to fit my 20” table loom. Finished measurements after finishing (handwash, tumble dry): 18.5” by 73” excluding fringe.",
    )
    project11_image1 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_25.jpg"
    )
    project11_image2 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_26.jpg"
    )
    project11_image3 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_27.jpg"
    )
    project11_image4 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_28.jpg"
    )
    project11_image5 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_29.jpg"
    )
    project11_image6 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_30.jpg"
    )
    project11_image7 = Project_Image(
        project_id=11,
        image_url="https://knotelry.s3.amazonaws.com/project_31.jpg"
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

    db.session.add(project7)
    db.session.add(project7_material1)
    db.session.add(project7_image1)
    db.session.add(project7_image2)

    db.session.add(project8)
    db.session.add(project8_material1)
    db.session.add(project8_image1)
    db.session.add(project8_image2)
    db.session.add(project8_image3)

    db.session.add(project9)
    db.session.add(project9_image1)
    db.session.add(project9_image2)

    db.session.add(project10)
    db.session.add(project10_image1)
    db.session.add(project10_image2)
    db.session.add(project10_image3)
    db.session.add(project10_image4)

    db.session.add(project11)
    db.session.add(project11_image1)
    db.session.add(project11_image2)
    db.session.add(project11_image3)
    db.session.add(project11_image4)
    db.session.add(project11_image5)
    db.session.add(project11_image6)
    db.session.add(project11_image7)

    db.session.commit()


def undo_projects():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE project_materials RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE project_tools RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE project_images RESTART IDENTITY CASCADE;')
