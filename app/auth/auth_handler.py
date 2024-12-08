import time
import jwt
from typing import Dict
from app.settings import settings


JWT_SECRET = settings.env_data.secret
JWT_ALGORITHM = settings.env_data.algorithm


def token_response(token: str) -> dict:
    return {
        "access_token": token
    }


def sing_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
