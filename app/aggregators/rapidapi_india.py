import requests
from datetime import datetime, timedelta
from config import RAPIDAPI_KEY, RAPIDAPI_HOST, DAYS_FILTER, TARGET_LOCATIONS

BASE_URL = f"https://{RAPIDAPI_HOST}/search"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST,
    "content-type": "application/json"
}

def fetch_rapidapi_jobs(query="jobs", page=1):
    params = {
        "query": query,
        "location": "Telangana",
        "page": page
    }

    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    data = response.json()

    cutoff = datetime.utcnow() - timedelta(days=DAYS_FILTER)
    jobs = []

    for job in data.get("data", []):  # structure varies by API
        location = job.get("location", "").lower()

        # Telangana location filter
        if not any(loc in location for loc in TARGET_LOCATIONS):
            continue

        # Date parsing (adjust depending on API format)
        posted_date_str = job.get("date_posted") or job.get("posted_at")

        try:
            posted_date = datetime.fromisoformat(
                posted_date_str.replace("Z", "")
            )
        except:
            continue

        if posted_date < cutoff:
            continue

        jobs.append({
            "source": "rapidapi",
            "id": job.get("id"),
            "title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("location"),
            "description": job.get("description"),
            "url": job.get("url"),
            "created_at": posted_date_str
        })

    return jobs