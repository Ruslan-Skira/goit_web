# OLD from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
   """
   The same as dotenv
   """
   sqlalchemy_database_url: str
   secret_key: str
   algorithm: str
   mail_username: str
   mail_password: str
   mail_from: str
   mail_port: int
   mail_server: str
   redis_host: str = 'localhost'
   redis_port: int = 6379
   postgres_db: str
   postgres_user: str
   postgres_password: str
   postgres_port: int


   class Config:
       env_file = ".env" # you could change here dev-test-stage
       env_file_encoding = "utf-8"


settings = Settings()