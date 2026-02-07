# Skillscout AI 🚀

SkillScout AI is an intelligent job discovery and matching backend built using **FastAPI**.
It aggregates jobs from multiple sources, matches them against user skills, and returns
ranked results using a scalable, production-ready architecture.

---

## 🧠 Why This Project?
Most job platforms show generic results.
SkillScout AI focuses on **skill-first matching**, performance, and explainability.

---

## 🏗️ Architecture Overview

Client
  → FastAPI Routes
    → Services Layer
      → Scrapers (Async & Concurrent)
      → Matching Engine
      → Cache
    → Response (Paginated, Scored)

---

## ⚙️ Tech Stack
- Python 3.11+
- FastAPI
- Pydantic
- AsyncIO
- In-memory caching (Redis-ready)
- Modular scraper architecture

---

## 🔑 Core Features
- Skill-based job matching
- Async concurrent job scraping
- Fault-tolerant scrapers (timeouts & isolation)
- Deterministic scoring engine
- Pagination & rate protection
- Clean service-based architecture

---

## 📡 API Endpoints

### Add Skills
POST `/api/v1/skills`
```json
{
  "skills": ["python", "fastapi"]
}
