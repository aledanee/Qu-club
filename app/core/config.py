from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str = '3306'  # Default MySQL port
    DATABASE_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()



