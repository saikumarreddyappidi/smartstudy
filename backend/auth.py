from datetime import datetime, timedelta
from typing import Optional
import base64
import hashlib
import hmac
import os
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
import models

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret_study_app_key_2024")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

PBKDF2_ITERATIONS = 390000


def _pbkdf2_hash(password: str, salt: bytes, iterations: int = PBKDF2_ITERATIONS) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)


def _encode_hash(iterations: int, salt: bytes, digest: bytes) -> str:
    salt_b64 = base64.urlsafe_b64encode(salt).decode("utf-8")
    digest_b64 = base64.urlsafe_b64encode(digest).decode("utf-8")
    return f"pbkdf2_sha256${iterations}${salt_b64}${digest_b64}"


def _parse_hash(hashed_password: str):
    parts = hashed_password.split("$")
    if len(parts) != 4 or parts[0] != "pbkdf2_sha256":
        raise ValueError("Invalid password hash format")
    iterations = int(parts[1])
    salt = base64.urlsafe_b64decode(parts[2].encode("utf-8"))
    digest = base64.urlsafe_b64decode(parts[3].encode("utf-8"))
    return iterations, salt, digest


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        iterations, salt, expected_digest = _parse_hash(hashed_password)
    except Exception:
        return False
    computed_digest = _pbkdf2_hash(plain_password, salt, iterations)
    return hmac.compare_digest(computed_digest, expected_digest)


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = _pbkdf2_hash(password, salt)
    return _encode_hash(PBKDF2_ITERATIONS, salt, digest)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
    except (JWTError, TypeError, ValueError):
        raise credentials_exception

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user
