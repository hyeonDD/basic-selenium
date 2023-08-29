from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TARGET_URL: str
    LOGIN_ID: EmailStr
    LOGIN_PASSWORD: str
    TIMEOUT: int

    class Config:
        env_file = ".env"


settings = Settings()

if __name__ == '__main__':
    print(settings.LOGIN_ID)
    print(settings.LOGIN_PASSWORD)
