from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Expense Tracker API"
    API_PREFIX: str = "/api"
    ENV: str = "development"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()