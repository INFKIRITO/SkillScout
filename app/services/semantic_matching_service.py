from typing import List, Optional
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.schemas.job import Job


class SemanticMatchingService:
    _model: Optional[SentenceTransformer] = None

    def _load_model(self):
        if self._model is None:
            self._model = SentenceTransformer("all-MiniLM-L6-v2")

    def score_jobs(self, jobs: List[Job], skills: List[str]) -> List[Job]:
        if not jobs or not skills:
            return jobs

        self._load_model()  # 👈 lazy load here

        skill_text = " ".join(skills)
        skill_embedding = self._model.encode([skill_text])

        job_texts = [
            f"{job.title} at {job.company}"
            for job in jobs
        ]
        job_embeddings = self._model.encode(job_texts)

        similarities = cosine_similarity(skill_embedding, job_embeddings)[0]

        for job, score in zip(jobs, similarities):
            job.score = float(score)

        jobs.sort(key=lambda j: j.score or 0, reverse=True)
        return jobs
