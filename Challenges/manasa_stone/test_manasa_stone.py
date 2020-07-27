import pytest
from manasa_stone import stones


@pytest.mark.parametrize("n, a, b, result",
                         [
                             (3, 1, 2, [2, 3, 4]),
                             (4, 10, 100, [30, 120, 210, 300]),
                         ]

                         )
def test_manastore(n, a, b, result):
    assert stones(n, a, b) == result
