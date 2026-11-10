from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Expense Tracker API"
    API_PREFIX: str = "/api"
    ENV: str = "development"
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/expense_tracker_db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()