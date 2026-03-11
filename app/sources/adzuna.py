import requests
from datetime import datetime, timedelta
from app.config import ADZUNA_APP_ID, ADZUNA_APP_KEY, DAYS_FILTER

def fetch_adzuna_jobs(country="in", page=1):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
    
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": 50,
        "where": "hyderabad, warangal, vizag, bangalore, chennai, pune, vijayawada",
        "what": "python developer, data engineer, ai engineer, machine learning, backend developer",
        "sort_by": "date",
        "max_days_old": DAYS_FILTER
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for job in data.get("results", []):
        jobs.append({
            "source": "adzuna",
            "id": job.get("id"),
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "url": job.get("redirect_url"),
            "created_at": job.get("created")
        })

    return jobs