import pytest

from src.password import Password

@pytest.fixture
def password() -> Password:
    return Password()
