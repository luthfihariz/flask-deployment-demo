from core.auth.ports import IHashingProvider, ITokenProvider
from infrastructure.auth.bcrypt import bcrypt


class BcryptHashingProvider(IHashingProvider):
    def generate(value: str) -> str:
        return bcrypt.generate_password_hash(value).decode('utf-8')     

    def check_hash(hashed_value: str, value: str) -> bool:
        return bcrypt.check_password_hash(hashed_value, value)