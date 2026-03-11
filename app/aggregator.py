from job_sources.google_search_jobs import fetch_google_jobs

def aggregate_jobs():
    all_jobs = []
    
    google_jobs = fetch_google_jobs()
    all_jobs.extend(google_jobs)

    # Remove duplicates by title + company
    unique = {(j["title"], j["company"]): j for j in all_jobs}

    return list(unique.values())