from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if settings.USE_SQLITE_DB == "True":
	SQLALCHEMY_DATABASE_URL = "sqlite:///./brygge.db"
	engine = create_engine(
		SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
	)
else:
	print("ERROR: not supported yet ... please use SQLite for this test")
	exit(-1)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()
