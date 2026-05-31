from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    prefix_version: str = "/api"
    version: str = "0.0.0"
    app_host: str = "localhost"
    app_port: int = 8000

    model_config = SettingsConfigDict(
        env_file = ".env"
    )

settings = Settings()