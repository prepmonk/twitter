# from passlib.context import CryptContext

# ctx = CryptContext(schemes=['bcrypt'], deprecated="auto") 
import base64

def hash_password(password: str):
    # return ctx.hash(password)
    return base64.b64encode(password.encode('utf-8'))

def verify_password(password: str, hashed_password: str):
    return base64.b64encode(password.encode('utf-8')) == hashed_password
    # return ctx.verify(password, hashed_password)
