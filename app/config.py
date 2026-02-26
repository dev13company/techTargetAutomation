import os

DATABASE_URL = os.getenv("DATABASE_URL")
VERCEL_NOTIFY_URL = os.getenv("VERCEL_NOTIFY_URL")
CRON_SECRET = os.getenv("CRON_SECRET")

KEYWORDS = [
    "python developer",
    "data engineer",
    "ai engineer",
    "machine learning",
    "backend developer"
]

MAX_JOB_AGE_DAYS = 3