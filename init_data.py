from db.base import Base
from db.session import DbSession,engine



Base.metadata.create_all(bind=engine)
print(2)

if __name__ == '__main__':
    print("1")