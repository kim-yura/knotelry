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
        length_stashed=150,
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
    fabric18 = Stash_Item(
        user_id=1,
        title="Poppy Fields",
        type="fabric",
        status="inStash",
        attributes="patterned",
        stored_in="Fabric closet",
        acquired_price=26,
        acquired_currency="USD",
        colors="red orange yellow green black ",
        dyer_name="Rifle Paper Co.",
        colorway_name="Poppy Fields Black",
        fiber_content="100% Cotton",
        fabric_width=44,
        fabric_width_unit="in",
        fabric_weight=4.2,
        fabric_weight_unit="oz",
        fabric_weight_area_unit="yd",
        fabric_pattern_repeat_width=12,
        fabric_pattern_repeat_height=9.26,
        fabric_pattern_repeat_unit="in",
        length_stashed=2,
        length_unit="yd",
    )
    fabric18_image1 = Stash_Item_Image(
        stash_item_id=18,
        image_url="https://knotelry.s3.amazonaws.com/stash_18.jpg",
    )
    fabric19 = Stash_Item(
        user_id=1,
        title="Lemon Grove",
        type="fabric",
        status="inStash",
        attributes="patterned",
        stored_in="Fabric closet",
        acquired_price=26,
        acquired_currency="USD",
        colors="yellow green purple white cream brown ",
        dyer_name="Rifle Paper Co.",
        colorway_name="Lemon Grove Cream Metallic",
        fiber_content="100% Cotton",
        fabric_width=44,
        fabric_width_unit="in",
        fabric_weight=4.2,
        fabric_weight_unit="oz",
        fabric_weight_area_unit="yd",
        fabric_pattern_repeat_width=8,
        fabric_pattern_repeat_height=8.75,
        fabric_pattern_repeat_unit="in",
        length_stashed=2,
        length_unit="yd",
    )
    fabric19_image1 = Stash_Item_Image(
        stash_item_id=19,
        image_url="https://knotelry.s3.amazonaws.com/stash_19.jpg",
    )
    fabric20 = Stash_Item(
        user_id=1,
        title="Eden",
        type="fabric",
        status="inStash",
        attributes="patterned",
        stored_in="Fabric closet",
        acquired_price=26,
        acquired_currency="USD",
        colors="orange green cream ",
        dyer_name="Rifle Paper Co.",
        colorway_name="Eden Cotton Red",
        fiber_content="100% Cotton",
        fabric_width=44,
        fabric_width_unit="in",
        fabric_weight=4.2,
        fabric_weight_unit="oz",
        fabric_weight_area_unit="yd",
        fabric_pattern_repeat_width=6,
        fabric_pattern_repeat_height=6.37,
        fabric_pattern_repeat_unit="in",
        length_stashed=2,
        length_unit="yd",
    )
    fabric20_image1 = Stash_Item_Image(
        stash_item_id=20,
        image_url="https://knotelry.s3.amazonaws.com/stash_20.jpg",
    )
    thread21 = Stash_Item(
        user_id=1,
        title="Gutermann Black",
        type="thread",
        status="inStash",
        stored_in="Sewing room",
        acquired_price=3.14,
        acquired_currency="USD",
        colors="black",
        dyer_name="Gutermann",
        colorway_name="Black",
        fiber_content="100% Polyester",
        length_per_bobbin=274,
        length_unit="yd",
        bobbins_stashed=2,
        length_stashed=548,
    )
    thread21_image1 = Stash_Item_Image(
        stash_item_id=21,
        image_url="https://knotelry.s3.amazonaws.com/stash_21.jpg",
    )
    thread22 = Stash_Item(
        user_id=1,
        title="Gutermann Turquoise",
        type="thread",
        status="inStash",
        stored_in="Sewing room",
        acquired_price=3.14,
        acquired_currency="USD",
        colors="bluegreen",
        dyer_name="Gutermann",
        colorway_name="Turquoise",
        fiber_content="100% Polyester",
        length_per_bobbin=274,
        length_unit="yd",
        bobbins_stashed=1,
        length_stashed=274,
    )
    thread22_image1 = Stash_Item_Image(
        stash_item_id=22,
        image_url="https://knotelry.s3.amazonaws.com/stash_22.jpg",
    )
    thread23 = Stash_Item(
        user_id=1,
        title="Gutermann Variegated",
        type="thread",
        status="inStash",
        stored_in="Sewing room",
        acquired_price=6.99,
        acquired_currency="USD",
        colors="purple white",
        dyer_name="Gutermann",
        colorway_name="Purple Passion",
        fiber_content="100% Cotton",
        length_per_bobbin=876,
        length_unit="yd",
        bobbins_stashed=1,
        length_stashed=876,
    )
    thread23_image1 = Stash_Item_Image(
        stash_item_id=23,
        image_url="https://knotelry.s3.amazonaws.com/stash_23.jpg",
    )
    thread24 = Stash_Item(
        user_id=1,
        title="Gutermann Upholstery Thread",
        type="thread",
        status="inStash",
        stored_in="Sewing room",
        acquired_price=4.54,
        acquired_currency="USD",
        colors="blue",
        dyer_name="Gutermann",
        colorway_name="Stone Blue",
        fiber_content="100% Polyester",
        length_per_bobbin=325,
        length_unit="yd",
        bobbins_stashed=1,
        length_stashed=325,
    )
    thread24_image1 = Stash_Item_Image(
        stash_item_id=24,
        image_url="https://knotelry.s3.amazonaws.com/stash_24.jpg",
    )
    fabric25 = Stash_Item(
        user_id=1,
        title="Cat Themed Fabric Pack",
        type="fabric",
        status="usedUp",
        colors="pink white gray",
        fiber_content="100% Cotton",
        length_stashed=2,
        length_unit="yd",
    )
    fabric25_image1 = Stash_Item_Image(
        stash_item_id=25,
        image_url="https://knotelry.s3.amazonaws.com/stash_25.jpg",
    )
    fabric26 = Stash_Item(
        user_id=1,
        title="Linen Fabric Pack from Korea",
        type="fabric",
        status="usedUp",
        colors="white gray cream",
        fiber_content="100% Linen",
        length_stashed=2,
        length_unit="yd",
    )
    fabric26_image1 = Stash_Item_Image(
        stash_item_id=26,
        image_url="https://knotelry.s3.amazonaws.com/stash_26.jpg",
    )
    aida27 = Stash_Item(
        user_id=1,
        title="Printed Watercolor Aida",
        type="aida",
        status="inStash",
        colors="bluegreen blue bluepurple purple white",
        fiber_content="100% Cotton",
        fabric_width=14,
        fabric_width_unit="in",
        fabric_height=10,
        fabric_height_unit="in",
        aida_count=14,
    )
    aida27_image1 = Stash_Item_Image(
        stash_item_id=27,
        image_url="https://knotelry.s3.amazonaws.com/stash_27.jpg",
    )
    aida28 = Stash_Item(
        user_id=1,
        title="Printed Nebula Aida",
        type="aida",
        status="usedUp",
        colors="blue bluepurple purpe white",
        fiber_content="100% Cotton",
        fabric_width=9.45,
        fabric_width_unit="in",
        fabric_height=9.45,
        fabric_height_unit="in",
        aida_count=16,
    )
    aida28_image1 = Stash_Item_Image(
        stash_item_id=28,
        image_url="https://knotelry.s3.amazonaws.com/stash_28.jpg",
    )
    aida29 = Stash_Item(
        user_id=1,
        title="Natural Aida Cloth",
        type="aida",
        status="inStash",
        colors="cream",
        fiber_content="100% Cotton",
        fabric_width=60,
        fabric_width_unit="in",
        fabric_height=2,
        fabric_height_unit="yd",
        aida_count=14,
    )
    aida29_image1 = Stash_Item_Image(
        stash_item_id=29,
        image_url="https://knotelry.s3.amazonaws.com/stash_29.jpg",
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

    db.session.add(fabric18)
    db.session.add(fabric18_image1)
    db.session.add(fabric19)
    db.session.add(fabric19_image1)
    db.session.add(fabric20)
    db.session.add(fabric20_image1)

    db.session.add(thread21)
    db.session.add(thread21_image1)
    db.session.add(thread22)
    db.session.add(thread22_image1)
    db.session.add(thread23)
    db.session.add(thread23_image1)
    db.session.add(thread24)
    db.session.add(thread24_image1)

    db.session.add(fabric25)
    db.session.add(fabric25_image1)
    db.session.add(fabric26)
    db.session.add(fabric26_image1)

    db.session.add(aida27)
    db.session.add(aida27_image1)
    db.session.add(aida28)
    db.session.add(aida28_image1)
    db.session.add(aida29)
    db.session.add(aida29_image1)

    db.session.add(test1)

    db.session.commit()


def undo_stash_items():
    db.session.execute('TRUNCATE stash RESTART IDENTITY CASCADE;')
    db.session.commit()
