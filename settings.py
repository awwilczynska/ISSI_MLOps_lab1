# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        allowed_envs = {"dev", "test", "prod"}
        if value not in allowed_envs:
            raise ValueError(
                f"ENVIRONMENT must be one of {allowed_envs}, got '{value}'"
            )
        return value
