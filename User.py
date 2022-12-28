import dataclasses

@dataclasses.dataclass
class User:
    """User class"""
    login: str
    mail: str
    password: str
    pp: str
