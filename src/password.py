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

    def __init__(self, length: int | None = None, delete: str = '') -> None:
        self.__password = PasswordGen.generate(length, delete)

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

    __CHARS = PasswordCharsSet()
    __RANGE = PasswordLengthRange()

    @classmethod
    def __delete_chars(cls, seq: str) -> tuple[str, ...]:
        if not seq:
            return cls.__CHARS.set

        chars: list[str] = list(PasswordGen.__CHARS.set)

        for index, chars_set in enumerate(chars):
            for s in seq:
                if s in chars_set:
                    chars[index] = chars[index].replace(s, '')

        return tuple(chars)


    @classmethod
    def generate(cls, length: int | None, delete: str) -> str:
        """Generates a random and secure password."""

        random_length = secrets.choice(
            range(cls.__RANGE.min, cls.__RANGE.max + 1)
        )

        _length = length if length else random_length

        chars = cls.__delete_chars(delete)

        password: list[str] = [
            secrets.choice(char_set) for char_set in chars
        ]

        chars = ''.join(chars)

        remaining_len = _length - len(password)

        password += [secrets.choice(chars) for _ in range(remaining_len)]

        return ''.join(
            secrets.SystemRandom().sample(password, k=len(password))
        )
