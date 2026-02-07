from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.schemas.job import Job


class SemanticMatchingService:
    def __init__(self):
        # Load once (cached in memory)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def score_jobs(self, jobs: List[Job], skills: List[str]) -> List[Job]:
        if not jobs or not skills:
            return jobs

        # Combine skills into a single semantic query
        skill_text = " ".join(skills)

        # Create embeddings
        skill_embedding = self.model.encode([skill_text])
        job_texts = [
            f"{job.title} at {job.company}"
            for job in jobs
        ]
        job_embeddings = self.model.encode(job_texts)

        # Compute cosine similarity
        similarities = cosine_similarity(skill_embedding, job_embeddings)[0]

        # Assign scores
        for job, score in zip(jobs, similarities):
            job.score = float(score)

        # Sort by relevance
        jobs.sort(key=lambda j: j.score or 0, reverse=True)
        return jobs
