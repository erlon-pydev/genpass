from typing import Literal

from src.password import Password, PasswordLengthRange, PasswordCharsSet


def test_Password_to_string(password: Password) -> None:
    assert isinstance(password.to_str(), str)
    assert isinstance(str(password), str)


def test_Password_casting_consistency(password: Password) -> None:
    assert password.to_str() == str(password)


def test_Password_length(password: Password) -> None:
    pwd_length = PasswordLengthRange()
    assert len(password)
    assert pwd_length.min <= len(password) <= pwd_length.max


def test_Password_chars(password: Password) -> None:
    chars_set: tuple[str, ...] = PasswordCharsSet().set

    check_chars: list[Literal[True, False]] = []

    for cs in chars_set:
        check_chars.append(
            any(char in cs for char in str(password))
        )

    assert all(check_chars)
