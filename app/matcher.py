from database import get_session

def match_jobs(jobs):
    session = get_session()

    matches = []

    for job in jobs:
        # Example: find candidates with matching skill
        query = """
        SELECT id FROM "Candidate"
        WHERE LOWER(skills) LIKE %s
        """

        result = session.execute(query, (f"%{job['title'].lower()}%",))

        for row in result:
            matches.append({
                "candidate_id": row[0],
                "job": job
            })

    session.close()
    return matches