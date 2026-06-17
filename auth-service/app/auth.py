from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "cms_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=60)

    payload = data.copy()
    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )