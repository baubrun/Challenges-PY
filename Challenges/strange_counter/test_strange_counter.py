import pytest
from strange_counter import strangeCounter


@pytest.mark.parametrize("t, result",
                         [
                             (4, 6),
                             (13,9),
                             (21, 1)
                         ]

                         )
def test_strangeCounter(t, result):
    assert strangeCounter(t) == result