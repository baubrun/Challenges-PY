import pytest
from add_single_num import add_up


@pytest.mark.parametrize("x, result",
                         [(4, 10), (13, 91), (600, 180300)]
                         )
def test_add_up(x, result):
    assert add_up(x) == result


@pytest.mark.parametrize("x, result",
                         [(4, 11), (13, 0), (0, 1)]
                         )
def test_add_up_neq(x, result):
    assert add_up(x) != result

