from flask.cli import AppGroup
from .users import seed_users, undo_users
from .tools import seed_tools, undo_tools
from .gallery_photos import seed_gallery_photos, undo_gallery_photos
from .stash_items import seed_stash_items, undo_stash_items
from .projects import seed_projects, undo_projects
from .groups import seed_groups, undo_groups

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_tools()
    seed_gallery_photos()
    seed_stash_items()
    seed_projects()
    seed_groups()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_tools()
    undo_gallery_photos()
    undo_stash_items()
    undo_projects()
    undo_groups()
    # Add other undo functions here
