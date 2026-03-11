from app.aggregators.adzuna import fetch_adzuna_jobs
from app.aggregators.muse import fetch_muse_jobs
from app.aggregators.rapidapi_india import fetch_rapidapi_jobs
from app.aggregators.deduplicator import deduplicate_jobs
from app.matching.semantic_matcher import match_jobs_with_resume


def run_pipeline():
    print("Fetching Adzuna jobs...")
    adzuna_jobs = fetch_adzuna_jobs(country="in")

    # print("Fetching Muse jobs...")
    # muse_jobs = fetch_muse_jobs()

    print("Fetching RapidAPI India jobs...")
    rapid_jobs = fetch_rapidapi_jobs(query="jobs")

    all_jobs = adzuna_jobs + rapid_jobs

    print(f"Total before deduplication: {len(all_jobs)}")

    unique_jobs = deduplicate_jobs(all_jobs)

    print(f"After deduplication: {len(unique_jobs)}")

    matched_jobs = match_jobs_with_resume(unique_jobs, resume_text)

    return matched_jobs

if __name__ == "__main__":
    run_pipeline()