import pytest
from karaca_encryption import encrypt


@pytest.mark.parametrize("x, result",

    [
        ("apple", "1lpp0aca"),
        ("karaca", "0c0r0kaca"),
        ("burak", "k0r3baca"),
        ("alpaca", "0c0pl0aca"),
    ]

)
def test_encrypt(x , result):
    assert encrypt(x) == result