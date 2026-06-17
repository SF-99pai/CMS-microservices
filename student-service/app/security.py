from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

SECRET_KEY = "cms_secret_key"
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(credentials=Depends(security)):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )