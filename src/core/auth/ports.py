from abc import ABC, abstractmethod

class ITokenProvider(ABC):

    @abstractmethod
    def generate_token(payload, secret_key):
        raise NotImplementedError
    
    @abstractmethod
    def verify_token(token, secret_key):
        raise NotImplementedError
    

class IHashingProvider(ABC):

    @abstractmethod
    def generate(value:str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def check_hash(hashed_value: str, value: str) -> bool:
        raise NotImplementedError