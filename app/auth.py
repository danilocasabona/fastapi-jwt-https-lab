from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException

SECRET_KEY = "segredo-super-forte"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_user = {
    "username": "danilo",
    "hashed_password": pwd_context.hash("Senha123")
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    if username != fake_user["username"]:
        return False
    if not verify_password(password, fake_user["hashed_password"]):
        return False
    return True

def create_jwt_token(username: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_MINUTES)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def validate_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")