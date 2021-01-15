from pydantic import BaseSettings, AnyHttpUrl
from typing import Optional


class Settings(BaseSettings):
    name = 1


settings = Settings(name=2)
def foo(a:int,b:int = 2) -> int:
    return a+b
def judge(result: bool) -> str:
 if result: return 'Error Occurred'

if __name__ == '__main__':
    # foo(1,'vvv')
    a = judge(False)
    print(a)
    print(settings.name)