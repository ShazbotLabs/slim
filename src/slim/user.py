"""The User class"""
from os import getlogin


class User:
    def __init__(self) -> None:
        self._username: str = getlogin()
    
    @property
    def username(self) -> str:
        return self._username
