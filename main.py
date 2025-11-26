import typer
import pyperclip

from src.password import Password


def main(
        length: int | None = None,
        delete: str = '',
        copy: bool = False,
        silent: bool = False
) -> None:
    password = Password(length, delete)

    if copy:
        pyperclip.copy(str(password))

    if copy and silent:
        pass
    else:
        print(password)


if __name__ == '__main__':
    typer.run(main)
