from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_jobs_with_resume(jobs, resume_text, threshold=0.6):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    matched_jobs = []

    for job in jobs:
        job_embedding = model.encode(job["description"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()

        if score >= threshold:
            job["match_score"] = score
            matched_jobs.append(job)

    return sorted(matched_jobs, key=lambda x: x["match_score"], reverse=True)