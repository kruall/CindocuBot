import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = 'CindocuBot'

DEBUG = False
TEST_GUILD_IDS = []
IMAGE_CHANNELS = []

TOKEN = os.getenv('TOKEN')
DEFAULT_PREFIXES = ['.']
INITIAL_EXTENSIONS = (
    'actions.restriction_cog',
    'eval.eval',
    'economy.economy',
    'economy.economy_control',
    'activity.text_activity',
    'activity.voice_activity',
    'relationship.relationship',
    'moderation.moderation',
    'personal_voice.controller',
    'history.history',
    'members.profile',
    'members.top',
    'members.welcome',
    'members.inventory_cog',
    'members.on_guild_cog',
    'members.role_controller',
    'suggestions.suggestions',
    'reputation.reputation',
    'premoderation.premoderation',
    'fun.fun',
    'game.play_cog',
    # ? 'ext.system.status',
    # ? 'ext.sync.sync',
    'up_listener.up_listener',
    'up_listener.up_reminder',
)

DATABASE = {
    'dbname': os.getenv('POSTGRES_NAME'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASS'),
}

LOGS_PATH = 'logs'
