import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
VERCEL_NOTIFY_URL = os.getenv("VERCEL_NOTIFY_URL")
CRON_SECRET = os.getenv("CRON_SECRET")
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")
DAYS_FILTER = int(os.getenv("DAYS_FILTER", 1))
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

KEYWORDS = [
    "python developer",
    "data engineer",
    "ai engineer",
    "machine learning",
    "backend developer"
]

MAX_JOB_AGE_DAYS = 7
DAYS_FILTER = 1

TARGET_LOCATIONS = [
    "hyderabad",
    "warangal",
    "vizag",
    "bangalore",
    "chennai",
    "pune",
    "vijayawada"
]