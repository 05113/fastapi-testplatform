from typing import Generator, Any, Union, Optional
from db.session import DbSession
def get_db() -> Generator:
    try:
        db = DbSession()
        yield db
    finally:
        db.close()
