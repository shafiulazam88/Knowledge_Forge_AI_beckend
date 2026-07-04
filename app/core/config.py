# from functools import lru_cache
# from pydantic_settings import BaseSettings , SettingsConfigDict

# class Settings(BaseSettings):
#         app_name: str 
#         app_version: str 
#         app_env: str 
#         debug: bool 
#         model_config = SettingsConfigDict(
#                 env_file = ".env",
#                 extra=  "ignore",
#         )

# @lru_cache()

# def get_settings() -> Settings:
#         return Settings()


from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_env: str
    debug: bool
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

@lru_cache()

def get_settings()-> Settings:
    return Settings()