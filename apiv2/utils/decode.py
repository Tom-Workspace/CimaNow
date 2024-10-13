from typing import Literal
from urllib.parse import quote, unquote


def decoding(type: Literal["encryption", "decrypt"], url: str) -> str:
    if type == "encryption":
        return quote(url)
    elif type == "decrypt":
        return unquote(url)
