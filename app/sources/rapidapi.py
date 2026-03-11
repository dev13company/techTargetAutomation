import requests
from datetime import datetime, timedelta
from app.config import RAPIDAPI_KEY, RAPIDAPI_HOST, DAYS_FILTER, TARGET_LOCATIONS

BASE_URL = f"https://{RAPIDAPI_HOST}/search"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}