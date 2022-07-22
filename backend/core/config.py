import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
	PROJECT_NAME: str = "BryggeTestLogin"
	PROJECT_VERSION: str = "1.0.0"

	USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")

	SECRET_KEY: str = os.getenv("SECRET_KEY")
	ALGORITHM: str = "HS256"
	ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins

	TEST_USER_EMAIL: str = "test@example.com"


settings = Settings()
