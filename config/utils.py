from typing import overload, Callable, TypeVar
from typing_extensions import Literal
import os


T = TypeVar('T')


@overload
def get_env(key: str, default: Literal[None] = None,
            *, allow_none: Literal[True], cast: Callable[[str | None], T]) -> T | None: ...


@overload
def get_env(key: str, default: str | None = None,
            allow_none: Literal[False] = False, *, cast: Callable[[str], T]) -> T: ...


@overload
def get_env(key: str, default: Literal[None] = None,
            allow_none: Literal[False] = False) -> str: ...


@overload
def get_env(key: str, default: Literal[None] = None,
            *, allow_none: Literal[True]) -> str | None: ...


@overload
def get_env(key: str, default: str,
            allow_none: Literal[False] = False) -> str: ...


def get_env(key: str, default: str | None = None, allow_none: bool = False, cast: Callable[[str], T] | Callable[[str | None], T] | None = None) -> str | None | T:
    val = os.getenv(key, default)
    if val is None and not allow_none:
        raise ValueError(f"Environment variable {
                         key} is not set with {allow_none}")
    return cast(val) if cast else val  # type: ignore


def boolean(value: str):
    return value.lower() in ["true", "1", "yes", "on"]
