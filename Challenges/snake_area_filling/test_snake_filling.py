import pytest
from snake_fill import snake_fill


@pytest.mark.parametrize("x, result",
                         [
                             (8, 6),
                             (18, 8),
                             (555, 18),
                             (2, 2),
                             (1, 0),
                             (900, 19)
                         ]

                         )
def test_strangeCounter(x, result):
    assert snake_fill(x) == result