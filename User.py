import dataclasses


@dataclasses
class User:
    """User class"""
    login: str
    mail: str
    password: str
    pp: str
