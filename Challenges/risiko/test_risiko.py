import pytest
from risiko import risiko

@pytest.mark.parametrize("a, d, result",
[
    ([3, 6, 4], [2, 5, 3], 3),
    ([3, 6], [6, 4, 4], 0),
    ([3, 1], [1], 1),
]

)


def test_risiko(a,d,result):
    assert risiko(a, d) == result