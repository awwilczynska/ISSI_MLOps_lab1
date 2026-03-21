import os
from main import export_envs
from settings import Settings


def test_settings():
    os.environ["API_KEY"] = "dummy_key"
    export_envs("test")
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "lab"
    assert settings.API_KEY == "dummy_key"
