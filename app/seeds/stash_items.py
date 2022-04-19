from app.models import db, Stash_Item, Stash_Item_Image



def seed_stash_items():
    fiber1 = Stash_Item(
        user_id=1,
        title="Mystery Corriedale OOAK and Merino in Carson",
        description="Fiber gifted to me from Malia Mayed It and Novamade",
        type="fiber",
        status="inStash",
        colors="yellowgreen green bluegreen blue purple ",
    )
    fiber1_image1 = Stash_Item_Image(
        stash_item_id=1,
        image_url="https://knotelry.s3.amazonaws.com/stash_1.jpg",
    )
    fiber2 = Stash_Item(
        user_id=1,
        title="Neon Gradient",
        type="fiber",
        status="usedUp",
        acquired_from="The Clay Purl in Nashville, Indiana",
        acquired_price=20.00,
        acquired_currency="USD",
        fiber_content="100% Wool, Merino",
        fiber_quantity=4,
        fiber_quantity_unit="oz",
        dyer_name="Bean Blossom Fibers",
        colors="yellow blue pink white rainbow",
    )
    fiber2_image1 = Stash_Item_Image(
        stash_item_id=2,
        image_url="https://knotelry.s3.amazonaws.com/stash_2.jpg",
    )
    fiber3 = Stash_Item(
        user_id=1,
        title="Partly Cloudy",
        type="fiber",
        status="usedUp",
        acquired_from="The Clay Purl in Nashville, Indiana",
        acquired_price=20.00,
        acquired_currency="USD",
        fiber_content="100% Wool, Merino",
        fiber_quantity=4,
        fiber_quantity_unit="oz",
        dyer_name="Bean Blossom Fibers",
        colors="blue white gray cream",
    )
    fiber3_image1=Stash_Item_Image(
        stash_item_id=3,
        image_url="https://knotelry.s3.amazonaws.com/stash_3.jpg",
    )
    fiber4 = Stash_Item(
        user_id=1,
        title="Lost Orchard Farm in Mystic Lakes",
        type="fiber",
        status="usedUp",
        acquired_from="Hoosier Hills Fiber Festival 2018",
        acquired_price=32.00,
        acquired_currency="USD",
        fiber_content="Bamboo Merino Silk",
        fiber_quantity=8,
        fiber_quantity_unit="oz",
        dyer_name="Lost Orchard Farm",
        colorway_name="Mystic Lakes",
        colors="bluegreen blue bluepurple purple",
    )
    fiber4_image1 = Stash_Item_Image(
        stash_item_id=4,
        image_url="https://knotelry.s3.amazonaws.com/stash_4.jpg",
    )
    yarn5 = Stash_Item(
        user_id=1,
        title="The Cozy Knitter Bliss",
        type="yarn",
        status="inStash",
        fiber_content="80% Merino, 20% Nylon",
        dyer_name="The Cozy Knitter",
        colorway_name="Sunkissed",
        yarn_weight="fingering",
        length_per_skein=420,
        length_unit="yd",
        weight_per_skein=115,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=420,
        weight_stashed=115,
        is_handspun=False,
        notes="Swap gift from Sabrina",
        colors="yellow gren blue pink white",
    )
    yarn5_image1 = Stash_Item_Image(
        stash_item_id=5,
        image_url="https://knotelry.s3.amazonaws.com/stash_5.jpg",
    )
    yarn6 = Stash_Item(
        user_id=1,
        title="Malabrigo Yarn Sock",
        type="yarn",
        status="inStash",
        acquired_from="Nomad Yarns in Plainfield, Indiana",
        fiber_content="100% Merino",
        dyer_name="Malabrigo",
        colorway_name="Diana",
        yarn_weight="lfingering",
        length_per_skein=440,
        length_unit="yd",
        weight_per_skein=100,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=440,
        weight_stashed=100,
        is_handspun=False,
        colors="red yellow green blue purple rainbow",
    )
    yarn6_image1 = Stash_Item_Image(
        stash_item_id=6,
        image_url="https://knotelry.s3.amazonaws.com/stash_6.jpg",
    )
    yarn7 = Stash_Item(
        user_id=1,
        title="Kelbourne Woolens Scout",
        type="yarn",
        status="inStash",
        acquired_from="Broad Ripple Knits in Indianapolis, Indiana",
        fiber_content="100% Wool",
        dyer_name="Kelbourne Woolens",
        colorway_name="Moss Heather",
        yarn_weight="dk",
        length_per_skein=274,
        length_unit="yd",
        weight_per_skein=100,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=274,
        weight_stashed=100,
        is_handspun=False,
        colors="green",
    )
    yarn7_image1 = Stash_Item_Image(
        stash_item_id=7,
        image_url="https://knotelry.s3.amazonaws.com/stash_7.jpg",
    )
    yarn8 = Stash_Item(
        user_id=1,
        title="3-Ply Traditional - First Try",
        type="yarn",
        status="usedUp",
        fiber_content="100% Wool",
        yarn_weight="fingering",
        length_per_skein=184,
        length_unit="yd",
        weight_per_skein=101,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=184,
        weight_stashed=101,
        is_handspun=True,
        colors="purple pink",
    )
    yarn8_image1 = Stash_Item_Image(
        stash_item_id=8,
        image_url="https://knotelry.s3.amazonaws.com/stash_8.jpg",
    )
    yarn9 = Stash_Item(
        user_id=1,
        title="Knit Picks Palette",
        type="yarn",
        status="inStash",
        colors="brown",
        dyer_name="Knit Picks",
        colorway_name="Bittersweet Heather",
        fiber_content="100% Wool",
        yarn_weight="fingering",
        length_per_skein=231,
        length_unit="yd",
        weight_per_skein=50,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=231,
        weight_stashed=50,
        is_handspun=False,
    )
    yarn9_image1 = Stash_Item_Image(
        stash_item_id= 9,
        image_url="https://knotelry.s3.amazonaws.com/stash_9.jpg"
    )
    yarn10= Stash_Item(
        user_id=1,
        title="Knit Picks Stroll Tweed",
        type="yarn",
        status="inStash",
        colors="orange",
        dyer_name="Knit Picks",
        colorway_name="Persimmon Heather",
        fiber_content="65% Merino, 25% Nylon, 10% Other",
        yarn_weight="fingering",
        length_per_skein=231,
        length_unit="yd",
        weight_per_skein=50,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=231,
        weight_stashed=50,
        is_handspun=False,
    )
    yarn10_image1 = Stash_Item_Image(
        stash_item_id=10,
        image_url="https://knotelry.s3.amazonaws.com/stash_10.jpg"
    )
    yarn11 = Stash_Item(
        user_id=1,
        title="Blossoms",
        type="yarn",
        status="inStash",
        colors="orange yellow bluegreen blue purple",
        dyer_name="Wonderland Yarns & Frabjous Fibers",
        colorway_name="Euphoria",
        fiber_content="80% Merino, 20% Nylon",
        yarn_weight="fingering",
        length_per_skein=425,
        length_unit="yd",
        weight_per_skein=113,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=425,
        weight_stashed=113,
        is_handspun=False,
    )
    yarn11_image1 = Stash_Item_Image(
        stash_item_id=11,
        image_url="https://knotelry.s3.amazonaws.com/stash_11.jpg"
    )
    yarn12 = Stash_Item(
        user_id=1,
        title="Wool of the Andes Worsted",
        type="yarn",
        status="inStash",
        colors="orange",
        dyer_name="Knit Picks",
        colorway_name="Persimmon Heather",
        fiber_content="100% Peruvian Highland Wool",
        yarn_weight="worsted",
        length_per_skein=110,
        length_unit="yd",
        weight_per_skein=50,
        weight_unit="g",
        skeins_stashed=16,
        length_stashed=1760,
        weight_stashed=50,
        is_handspun=False,
    )
    yarn12_image1 = Stash_Item_Image(
        stash_item_id=12,
        image_url="https://knotelry.s3.amazonaws.com/stash_12.jpg"
    )
    yarn13 = Stash_Item(
        user_id=1,
        title="Baseline",
        type="yarn",
        status="inStash",
        colors="purple pink",
        dyer_name="Graphic Dyeworks",
        colorway_name="Loganberry",
        fiber_content="80% Merino, 20% Nylon",
        yarn_weight="fingering",
        length_per_skein=400,
        length_unit="yd",
        weight_per_skein=100,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=400,
        weight_stashed=100,
        is_handspun=False,
        notes="Gifted to me by the dyer."
    )
    yarn13_image1 = Stash_Item_Image(
        stash_item_id=13,
        image_url="https://knotelry.s3.amazonaws.com/stash_13.jpg",
    )
    yarn14 = Stash_Item(
        user_id=1,
        title="Rowan Softyak DK",
        type="yarn",
        status="inStash",
        colors="pink",
        dyer_name="Rowan",
        colorway_name="Meadow",
        fiber_content="76% Cotton, 15% Yak, 9% Nylon",
        yarn_weight="dk",
        length_per_skein=148,
        length_unit="yd",
        weight_per_skein=50,
        weight_unit="g",
        skeins_stashed=3,
        length_stashed=444,
        weight_stashed=50,
        is_handspun=False,
        notes="Won from Claud's Halloween giveaway."
    )
    yarn14_image1 = Stash_Item_Image(
        stash_item_id=14,
        image_url="https://knotelry.s3.amazonaws.com/stash_14.jpg",
    )
    yarn15 = Stash_Item(
        user_id=1,
        title="Wool and Vinyl Hard Rock DK",
        type="yarn",
        status="inStash",
        colors="yellow green bluegreen blue pink white",
        dyer_name="Wool and Vinyl",
        colorway_name="Walkin to New Orleans",
        fiber_content="100% Merino",
        yarn_weight="dk",
        length_per_skein=250,
        length_unit="yd",
        weight_per_skein=115,
        weight_unit="g",
        skeins_stashed=1,
        length_stashed=115,
        weight_stashed=115,
        is_handspun=False,
        notes="Purchased while in New Orleans for a conference."
    )
    yarn15_image1 = Stash_Item_Image(
        stash_item_id=15,
        image_url="https://knotelry.s3.amazonaws.com/stash_15.jpg",
    )
    fiber16 = Stash_Item(
        user_id=1,
        title="Koomasee Fiber",
        type="fiber",
        status="usedUp",
        acquired_price=26.75,
        acquired_currency="USD",
        fiber_content="100% Wool, Merino",
        fiber_quantity=4,
        fiber_quantity_unit="oz",
        dyer_name="Koomasee Fiber",
        colors="red orange blue purple white",
    )
    fiber16_image1 = Stash_Item_Image(
        stash_item_id=16,
        image_url="https://knotelry.s3.amazonaws.com/stash_16.jpg",
    )
    fiber17 = Stash_Item(
        user_id=1,
        title="Koomasee Fiber",
        type="fiber",
        status="usedUp",
        acquired_price=26.75,
        acquired_currency="USD",
        fiber_content="100% Wool, Merino",
        fiber_quantity=4,
        fiber_quantity_unit="oz",
        dyer_name="Koomasee Fiber",
        colors="orange yellow yellowgreen green blue white",
    )
    fiber17_image1 = Stash_Item_Image(
        stash_item_id=17,
        image_url="https://knotelry.s3.amazonaws.com/stash_17.jpg",
    )
    test1 = Stash_Item(
        user_id=2,
        title="Not DemoUser's stash"
    )

    db.session.add(fiber1)
    db.session.add(fiber1_image1)
    db.session.add(fiber2)
    db.session.add(fiber2_image1)
    db.session.add(fiber3)
    db.session.add(fiber3_image1)
    db.session.add(fiber4)
    db.session.add(fiber4_image1)

    db.session.add(yarn5)
    db.session.add(yarn5_image1)
    db.session.add(yarn6)
    db.session.add(yarn6_image1)
    db.session.add(yarn7)
    db.session.add(yarn7_image1)
    db.session.add(yarn8)
    db.session.add(yarn8_image1)
    db.session.add(yarn9)
    db.session.add(yarn9_image1)
    db.session.add(yarn10)
    db.session.add(yarn10_image1)
    db.session.add(yarn11)
    db.session.add(yarn11_image1)
    db.session.add(yarn12)
    db.session.add(yarn12_image1)
    db.session.add(yarn13)
    db.session.add(yarn13_image1)
    db.session.add(yarn14)
    db.session.add(yarn14_image1)
    db.session.add(yarn15)
    db.session.add(yarn15_image1)

    db.session.add(fiber16)
    db.session.add(fiber16_image1)
    db.session.add(fiber17)
    db.session.add(fiber17_image1)

    db.session.add(test1)

    db.session.commit()


def undo_stash_items():
    db.session.execute('TRUNCATE stash RESTART IDENTITY CASCADE;')
    db.session.commit()
