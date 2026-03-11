def deduplicate_jobs(jobs):
    seen = set()
    unique_jobs = []

    for job in jobs:
        unique_key = (
            job["url"] or 
            (job["title"].lower().strip() + job["company"].lower().strip())
        )

        if unique_key not in seen:
            seen.add(unique_key)
            unique_jobs.append(job)

    return unique_jobs