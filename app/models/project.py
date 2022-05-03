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
    # finished_length
    # length_unit
    finished_weight = db.Column(db.Float)
    weight_unit = db.Column(db.String(2))

    # Weaving
    warp_yarn = db.Column(db.String(100))
    weft_yarn = db.Column(db.String(100))
    epi = db.Column(db.Float)
    total_ends = db.Column(db.Integer)
    ppi = db.Column(db.Float)
    draft_notes = db.Column(db.Text)
    width_in_reed = db.Column(db.Float)
    length = db.Column(db.Float)
    length_unit = db.Column(db.String(2))
    finished_length = db.Column(db.Float)

    # Knitting
    needle_sizes = db.Column(db.Text)
    gauge_count = db.Column(db.Integer)
    gauge_unit = db.Column(db.String(4))
    gauge_rows = db.Column(db.Integer)
    gauge_size_width = db.Column(db.Integer)
    gauge_size_height = db.Column(db.Integer)
    gauge_size_unit = db.Column(db.String(2))

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
            'finished_weight': self.finished_weight,
            'weight_unit': self.weight_unit,

            'warp_yarn': self.warp_yarn,
            'weft_yarn': self.weft_yarn,
            'epi': self.epi,
            'total_ends': self.total_ends,
            'ppi': self.ppi,
            'draft_notes': self.draft_notes,
            'width_in_reed': self.width_in_reed,
            'length': self.length,
            'length_unit': self.length_unit,
            'finished_length': self.finished_length,

            'needle_sizes': self.needle_sizes,
            'gauge_count': self.gauge_count,
            'gauge_unit': self.gauge_unit,
            'gauge_rows': self.gauge_rows,
            'gauge_size_width': self.gauge_size_width,
            'gauge_size_height': self.gauge_size_height,
            'gauge_size_unit': self.gauge_size_unit,

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
            'finishedWeight': self.finished_weight,
            'weightUnit': self.weight_unit,

            'warpYarn': self.warp_yarn,
            'weftYarn': self.weft_yarn,
            'epi': self.epi,
            'totalEnds': self.total_ends,
            'ppi': self.ppi,
            'draftNotes': self.draft_notes,
            'widthInReed': self.width_in_reed,
            'length': self.length,
            'lengthUnit': self.length_unit,
            'finishedLength': self.finished_length,

            'needleSizes': self.needle_sizes,
            'gaugeCount': self.gauge_count,
            'gaugeUnit': self.gauge_unit,
            'gaugeRows': self.gauge_rows,
            'gaugeSizeWidth': self.gauge_size_width,
            'gaugeSizeHeight': self.gauge_size_height,
            'gaugeSizeUnit': self.gauge_size_unit,

            'notes': self.notes,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,

            'user': self.user.to_JSON(),
            'projectMaterials': [material.to_JSON() for material in self.project_material],
            'projectTools': [tool.to_JSON() for tool in self.project_tool],
            'projectImages': [image.to_JSON() for image in self.project_image]
        }
