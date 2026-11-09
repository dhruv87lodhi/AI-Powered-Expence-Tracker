# AI-Powered Expense Tracker - Learning & Context Log

## Architecture Overview
- **Backend**: FastAPI (Python 3.11)
- **Database**: PostgreSQL
- **ORM & Migrations**: SQLAlchemy & Alembic
- **Pattern**: 3-Tier Layered Architecture (Routes -> Services -> Repositories -> Models)

---

## Milestone 0: Project Hygiene & Setup
### 1. Git Hygiene (`.gitignore`)
- Learned why `.gitignore` is crucial:
  - **`__pycache__/`**: Avoid committing machine-specific compiled Python bytecode.
  - **`venv/`**: Avoid committing massive local dependencies; teammates should install fresh packages instead.
  - **`.env`**: Protect database credentials and secret keys from ever being exposed to GitHub.