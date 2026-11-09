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

  
## Milestone 1: Minimal Working API Server
- **What Was Done**:
  - Added `fastapi` and `uvicorn` to `Backend/requirements.txt` and installed them in the virtual environment.
  - Created entry point in `Backend/app/main.py` with an `@app.get("/")` root route.
  - Ran the server with `uvicorn app.main:app --reload`.
  - Verified JSON response and explored the auto-generated Swagger UI at `/docs`.
- **Key Concepts Learned**:
  - **FastAPI vs Uvicorn**: FastAPI provides routing and business logic; Uvicorn is the ASGI web server that listens on network ports.
  - **Auto-Reload (`--reload`)**: Automatically reloads the development server whenever code is saved.
  - **Automatic OpenAPI / Swagger**: FastAPI generates interactive API documentation without writing separate docs.

  
## Milestone 2: Configuration & Environment Management
- **What Was Done**:
  - Added `pydantic-settings` to manage application configuration.
  - Created `Backend/app/core/config.py` using `BaseSettings` to declare strongly-typed settings (`PROJECT_NAME`, `API_PREFIX`, `ENV`).
  - Created `Backend/.env.example` as a public template and `Backend/.env` for local configuration.
  - Connected `settings` into `Backend/app/main.py` and verified live overriding.
- **Key Concepts Learned**:
  - **12-Factor App Config**: Never hardcode configuration or credentials in source code.
  - **Pydantic BaseSettings**: Strongly-typed settings validation that automatically reads from environment variables and `.env` files.
  - **`.env` vs `.env.example`**: `.env.example` is committed to document expected variables; `.env` holds actual machine secrets and is ignored by Git.