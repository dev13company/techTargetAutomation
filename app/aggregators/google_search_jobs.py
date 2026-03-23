import requests
from bs4 import BeautifulSoup
from datetime import datetime
from config import KEYWORDS

BASE_URL = "https://www.google.com/search?q="

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_google_jobs():
    jobs = []

    for keyword in KEYWORDS:
        url = f"{BASE_URL}{keyword.replace(' ', '+')}+jobs&hl=en"
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")

        results = soup.find_all("div", class_="BVG0Nb")

        for job in results:
            title = job.find("div", class_="BjJfJf PUpOsf")
            company = job.find("div", class_="vNEEBe")
            location = job.find("div", class_="Qk80Jf")

            if title:
                jobs.append({
                    "title": title.text,
                    "company": company.text if company else "",
                    "location": location.text if location else "",
                    "source": "Google Jobs",
                    "scraped_at": datetime.utcnow()
                })

    return jobs