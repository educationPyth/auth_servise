from environs import Env
from dataclasses import dataclass


@dataclass
class SecretData:
    secret: str
    algorithm: str


@dataclass
class Settings:
    env_data: SecretData


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        env_data=SecretData(
            secret=env.str('SECRET'),
            algorithm=env.str('ALGORITHM')
        )
    )


settings = get_settings('input')