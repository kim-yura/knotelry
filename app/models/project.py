from .db import db
from datetime import datetime


class Project_Material(db.Model):
    __tablename__ = 'project_materials'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    stash_id = db.Column(db.Integer, db.ForeignKey('stash.id'))

    fiber_quantity_used = db.Column(db.Float)
    fiber_quantity_unit = db.Column(db.String(5))
    length_used = db.Column(db.Float)
    length_unit = db.Column(db.String(5))
    weight_used = db.Column(db.Float)
    weight_unit = db.Column(db.String(5))
    skeins_used = db.Column(db.Float)
    units_used = db.Column(db.Float)

    project = db.relationship('Project', back_populates='project_material')
    stash_item = db.relationship('Stash_Item', back_populates='project_material')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'stash_id': self.stash_id,
            'fiber_quantity_used': self.fiber_quantity_used,
            'fiber_quantity_unit': self.fiber_quantity_unit,
            'length_used': self.length_used,
            'length_unit': self.length_unit,
            'weight_used': self.weight_used,
            'weight_unit': self.weight_unit,
            'skeins_used': self.skeins_used,
            'units_used': self.units_used,
            'stash_item': self.stash_item.to_dict(),
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'projectId': self.project_id,
            'stashId': self.stash_id,
            'fiberQuantityUsed': self.fiber_quantity_used,
            'fiberQuantityUnit': self.fiber_quantity_unit,
            'lengthUsed': self.length_used,
            'lengthUnit': self.length_unit,
            'weightUsed': self.weight_used,
            'weightUnit': self.weight_unit,
            'skeinsUsed': self.skeins_used,
            'unitsUsed': self.units_used,
            'stashItem': self.stash_item.to_JSON(),
        }



class Project_Tool(db.Model):
    __tablename__ = 'project_tools'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    tool_id = db.Column(db.Integer, db.ForeignKey('tools.id'))

    project = db.relationship('Project', back_populates='project_tool')
    tool = db.relationship('Tool', back_populates='project_tool')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'tool_id': self.tool_id,
            'tool_item': self.tool.to_dict(),
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'projectId': self.project_id,
            'toolId': self.tool_id,
            'toolItem': self.tool.to_JSON(),
        }



class Project_Image(db.Model):
    __tablename__ = 'project_images'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    image_url = db.Column(db.String(100))

    project = db.relationship('Project', back_populates='project_image')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'image_url': self.image_url,
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'projectId': self.project_id,
            'imageURL': self.image_url,
        }



class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Metadata
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    craft_types = db.Column(db.String(50))

    pattern_name = db.Column(db.String(100))
    pattern_author = db.Column(db.String(500))
    link_to_pattern = db.Column(db.Text)
    size_made = db.Column(db.String(20))

    tags = db.Column(db.Text)
    status = db.Column(db.String(50))
    attributes = db.Column(db.Text)
    stored_in = db.Column(db.Text)

    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    # Spinning
    yarn_weight = db.Column(db.String(20))
    grist = db.Column(db.Float)
    grist_unit = db.Column(db.String(5))
    wpi = db.Column(db.Integer)
    plies_count = db.Column(db.Integer)

    twist_direction_singles = db.Column(db.String(1))
    twist_direction_plied = db.Column(db.String(1))
    twist_angle = db.Column(db.Float)
    drive_ratio_singles = db.Column(db.Integer)
    drive_ratio_plied = db.Column(db.Integer)
    finished_yarn_length = db.Column(db.Integer)
    finished_yarn_length_unit = db.Column(db.String(2))
    finished_yarn_weight = db.Column(db.Float)
    finished_yarn_weight_unit = db.Column(db.String(2))

    # Weaving
    warp_yarn = db.Column(db.String(100))
    weft_yarn = db.Column(db.String(100))
    epi = db.Column(db.Float)
    ppi = db.Column(db.Float)
    total_ends = db.Column(db.Integer)
    draft_notes = db.Column(db.Text)

    width_in_reed = db.Column(db.Float)
    width_in_reed_unit = db.Column(db.String(2))
    warped_length = db.Column(db.Float)
    warped_length_unit = db.Column(db.String(2))
    length = db.Column(db.Float)
    length_unit = db.Column(db.String(2))
    finished_length = db.Column(db.Float)
    finished_length_unit = db.Column(db.String(2))
    finished_width = db.Column(db.Float)
    finished_width_unit = db.Column(db.String(2))

    # Knitting
    needle_sizes = db.Column(db.Text)
    knit_gauge_count = db.Column(db.Integer)
    knit_gauge_unit = db.Column(db.String(4))
    knit_gauge_rows = db.Column(db.Integer)
    knit_gauge_size_width = db.Column(db.Integer)
    knit_gauge_size_height = db.Column(db.Integer)
    knit_gauge_size_unit = db.Column(db.String(2))

    # Crocheting
    hook_sizes = db.Column(db.Text)
    crochet_gauge_count = db.Column(db.Integer)
    crochet_gauge_unit = db.Column(db.String(4))
    crochet_gauge_rows = db.Column(db.Integer)
    crochet_gauge_size_width = db.Column(db.Integer)
    crochet_gauge_size_height = db.Column(db.Integer)
    crochet_gauge_size_unit = db.Column(db.String(2))

    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # Relationships
    user = db.relationship('User', back_populates='project')
    project_material = db.relationship('Project_Material', back_populates='project', cascade='all, delete-orphan')
    project_tool = db.relationship('Project_Tool', back_populates='project', cascade='all, delete-orphan')
    project_image = db.relationship('Project_Image', back_populates='project', cascade='all, delete-orphan')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,

            'title': self.title,
            'description': self.description,
            'craft_types': self.craft_types,
            'pattern_name': self.pattern_name,
            'pattern_author': self.pattern_author,
            'link_to_pattern': self.link_to_pattern,
            'size_made': self.size_made,
            'tags': self.tags,
            'status': self.status,
            'attributes': self.attributes,
            'stored_in': self.stored_in,
            'start_date': self.start_date,
            'end_date': self.end_date,

            'yarn_weight': self.yarn_weight,
            'grist': self.grist,
            'grist_unit': self.grist_unit,
            'wpi': self.wpi,
            'plies_count': self.plies_count,
            'twist_direction_singles': self.twist_direction_singles,
            'twist_direction_plied': self.twist_direction_plied,
            'twist_angle': self.twist_angle,
            'drive_ratio_singles': self.drive_ratio_singles,
            'drive_ratio_plied': self.drive_ratio_plied,
            'finished_yarn_length': self.finished_yarn_length,
            'finished_yarn_length_unit': self.finished_yarn_length_unit,
            'finished_yarn_weight': self.finished_yarn_weight,
            'finished_yarn_weight_unit': self.finished_yarn_weight_unit,

            'warp_yarn': self.warp_yarn,
            'weft_yarn': self.weft_yarn,
            'epi': self.epi,
            'ppi': self.ppi,
            'total_ends': self.total_ends,
            'draft_notes': self.draft_notes,

            'length': self.length,
            'length_unit': self.length_unit,
            'width_in_reed': self.width_in_reed,
            'width_in_reed_unit': self.width_in_reed_unit,
            'warped_length': self.warped_length,
            'warped_length_unit': self.warped_length_unit,
            'finished_length': self.finished_length,
            'finished_length_unit': self.finished_length_unit,
            'finished_width': self.finished_width,
            'finished_width_unit': self.finished_width_unit,

            'needle_sizes': self.needle_sizes,
            'knit_gauge_count': self.knit_gauge_count,
            'knit_gauge_unit': self.knit_gauge_unit,
            'knit_gauge_rows': self.knit_gauge_rows,
            'knit_gauge_size_width': self.knit_gauge_size_width,
            'knit_gauge_size_height': self.knit_gauge_size_height,
            'knit_gauge_size_unit': self.knit_gauge_size_unit,

            'hook_sizes': self.hook_sizes,
            'crochet_gauge_count': self.crochet_gauge_count,
            'crochet_gauge_unit': self.crochet_gauge_unit,
            'crochet_gauge_rows': self.crochet_gauge_rows,
            'crochet_gauge_size_width': self.crochet_gauge_size_width,
            'crochet_gauge_size_height': self.crochet_gauge_size_height,
            'crochet_gauge_size_unit': self.crochet_gauge_size_unit,

            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at,

            'user': self.user.to_dict(),
            'project_materials': [material.to_dict() for material in self.project_material],
            'project_tools': [tool.to_dict() for tool in self.project_tool],
            'project_images': [image.to_dict() for image in self.project_image],
        }

    def to_JSON(self):
        return {
            'id': self.id,
            'userId': self.user_id,

            'title': self.title,
            'description': self.description,
            'craftTypes': self.craft_types,
            'patternName': self.pattern_name,
            'patternAuthor': self.pattern_author,
            'linkToPattern': self.link_to_pattern,
            'sizeMade': self.size_made,
            'tags': self.tags,
            'status': self.status,
            'attributes': self.attributes,
            'storedIn': self.stored_in,
            'startDate': self.start_date,
            'endDate': self.end_date,

            'yarnWeight': self.yarn_weight,
            'grist': self.grist,
            'gristUnit': self.grist_unit,
            'wpi': self.wpi,
            'pliesCount': self.plies_count,
            'twistDirectionSingles': self.twist_direction_singles,
            'twistDirectionPlied': self.twist_direction_plied,
            'twistAngle': self.twist_angle,
            'driveRatioSingles': self.drive_ratio_singles,
            'driveRatioPlied': self.drive_ratio_plied,
            'finishedYarnLength': self.finished_yarn_length,
            'finishedYarnLengthUnit': self.finished_yarn_length_unit,
            'finishedYarnWeight': self.finished_yarn_weight,
            'finishedYarnWeightUnit': self.finished_yarn_weight_unit,

            'warpYarn': self.warp_yarn,
            'weftYarn': self.weft_yarn,
            'epi': self.epi,
            'ppi': self.ppi,
            'totalEnds': self.total_ends,
            'draftNotes': self.draft_notes,

            'length': self.length,
            'lengthUnit': self.length_unit,
            'widthInReed': self.width_in_reed,
            'widthInReedUnit': self.width_in_reed_unit,
            'warpedLength': self.warped_length,
            'warpedLengthUnit': self.warped_length_unit,
            'finishedLength': self.finished_length,
            'finishedLengthUnit': self.finished_length_unit,
            'finishedWidth': self.finished_width,
            'finishedWidthUnit': self.finished_width_unit,

            'needleSizes': self.needle_sizes,
            'knitGaugeCount': self.knit_gauge_count,
            'knitGaugeUnit': self.knit_gauge_unit,
            'knitGaugeRows': self.knit_gauge_rows,
            'knitGaugeSizeWidth': self.knit_gauge_size_width,
            'knitGaugeSizeHeight': self.knit_gauge_size_height,
            'knitGaugeSizeUnit': self.knit_gauge_size_unit,

            'hookSizes': self.hook_sizes,
            'crochetGaugeCount': self.crochet_gauge_count,
            'crochetGaugeUnit': self.crochet_gauge_unit,
            'crochetGaugeRows': self.crochet_gauge_rows,
            'crochetGaugeSizeWidth': self.crochet_gauge_size_width,
            'crochetGaugeSizeHeight': self.crochet_gauge_size_height,
            'crochetGaugeSizeUnit': self.crochet_gauge_size_unit,

            'notes': self.notes,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,

            'user': self.user.to_JSON(),
            'projectMaterials': [material.to_JSON() for material in self.project_material],
            'projectTools': [tool.to_JSON() for tool in self.project_tool],
            'projectImages': [image.to_JSON() for image in self.project_image]
        }
