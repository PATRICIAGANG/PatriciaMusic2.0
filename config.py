from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQACJAZpk6po5G4xYnfXxo5gtfJ9MFrJSJWyDnnAuA32lU9HrXzZR7jZR73MUw5Rf6lHJ5AHwS5rRItd6W7soE3wAHU5uWjj2RBUlV_dTyYHEA6PIYKmoo0HxSwZjIbeh9PBimDVExqpstBLYS97tOi1czCu_xx6j3kfymu0Bpz5PD53KBDQMFmqiFhXjdr83OEyjYLDpr79wAqm5Ti4eAjGPY62o7DdyzEgN-wid92ua89x2y5lI4tEn-6Q264ezo6m_egD5lRLsVvmNEq2PVy405bPZokxtkVe7cCerQHxnySnkyqAQzKCm940_ASO4lq9MzIZmTQPBKlJ-kEh82I7b6crEAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAHInQ7dfJflnXulngXqva33-djG7xiIjwM")
BOT_NAME = getenv("BOT_NAME", "PATRICIA")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "80"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
