from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    prefix_version: str = ""
    version: str = ""
    app_host: str = ""
    app_port: int = 0
    secret_key: str = ""
    algorithm: str = ""

    model_config = SettingsConfigDict(
        env_file = ".env"
    )

settings = Settings()