from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from starlette import status

from db import get_db, User
class Hash:
   pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

   def verify_password(self, plain_password, hashed_password):
       return self.pwd_context.verify(plain_password, hashed_password)

   def get_password_hash(self, password: str):
       return self.pwd_context.hash(password)

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# define a function to generate a new access token
async def create_access_token(data: dict, expires_delta: Optional[float] = None):
   to_encode = data.copy()
   if expires_delta:
       expire = datetime.utcnow() + timedelta(seconds=expires_delta)
   else:
       expire = datetime.utcnow() + timedelta(minutes=365)
   to_encode.update({"exp": expire})
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
   return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
   credentials_exception = HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
       detail="Could not validate credentials",
       headers={"WWW-Authenticate": "Bearer"},
   )

   try:
       # Decode JWT
       payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       email = payload["sub"]
       if email is None:
           raise credentials_exception
   except JWTError as e:
       raise credentials_exception

   user: User = db.query(User).filter(User.email == email).first()
   if user is None:
       raise credentials_exception
   return user