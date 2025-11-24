import secrets
from dataclasses import dataclass
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


@dataclass(slots=True, frozen=True)
class PasswordLengthRange:
    min = 16
    max = 32


@dataclass(slots=True, frozen=True)
class PasswordCharsSet:
    set: tuple[str, ...] = (
        ascii_lowercase,
        ascii_uppercase,
        digits,
        punctuation,
    )

class Password:
    """Password Generator"""

    __slots__ = ('__password',)

    def __init__(self) -> None:
        self.__password = PasswordGen.generate()

    def __str__(self) -> str:
        return self.__password

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}>'

    def __len__(self) -> int:
        return len(self.__password)

    def to_str(self) -> str:
        return self.__password


class PasswordGen:
    """Password Generator"""

    __slots__ = ()

    __RANGE = PasswordLengthRange()
    __LENGTH = secrets.choice(range(__RANGE.min, __RANGE.max + 1))
    __CHARS = PasswordCharsSet()

    @staticmethod
    def generate() -> str:
        """Generates a random and secure password."""

        password: list[str] = [
            secrets.choice(char_set) for char_set in PasswordGen.__CHARS.set
        ]

        chars = ''.join(PasswordGen.__CHARS.set)

        remaining_len = PasswordGen.__LENGTH - len(password)

        password += [secrets.choice(chars) for _ in range(remaining_len)]

        return ''.join(
            secrets.SystemRandom().sample(password, k=len(password))
        )
