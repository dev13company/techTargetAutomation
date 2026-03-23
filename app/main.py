from aggregators.adzuna import fetch_adzuna_jobs
# from aggregators.muse import fetch_muse_jobs
# from aggregators.rapidapi_india import fetch_rapidapi_jobs
from util.deduplicator import deduplicate_jobs
# from matcher.semantic_matcher import match_jobs_with_resume


def run_pipeline():
    print("Fetching Adzuna jobs...")
    adzuna_jobs = fetch_adzuna_jobs(country="in")

    # print("Fetching Muse jobs...")
    # muse_jobs = fetch_muse_jobs()

    print("Fetching RapidAPI India jobs...")
    # rapid_jobs = fetch_rapidapi_jobs(query="jobs")

    all_jobs = adzuna_jobs #+ rapid_jobs

    print(f"Total before deduplication: {len(all_jobs)}")

    unique_jobs = deduplicate_jobs(all_jobs)

    print(f"After deduplication: {len(unique_jobs)}")

    # matched_jobs = match_jobs_with_resume(unique_jobs, resume_text)

    return unique_jobs

if __name__ == "__main__":
    unique_jobs = run_pipeline()
    print(unique_jobs)