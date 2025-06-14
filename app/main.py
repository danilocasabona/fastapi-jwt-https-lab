from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from app.models import LoginRequest
from app.auth import authenticate_user, create_jwt_token, validate_jwt

app = FastAPI()

security = HTTPBearer()

@app.post("/login")
def login(login_req: LoginRequest):
    if not authenticate_user(login_req.username, login_req.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_jwt_token(login_req.username)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protegido")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = validate_jwt(token)
    return {"msg": f"Bem-vindo {user}, acesso autorizado!"}