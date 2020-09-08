import pytest
from rps import rps


@pytest.mark.parametrize("p1, p2, result",
                         [
                             ("Rock", "Paper", "The winner is p2"),
                             ("Scissors", "Paper", "The winner is p1"),
                             ("Paper", "Paper", "It's a draw"),
                         ]

                         )
def test_missing_num(p1, p2, result):
    assert rps(p1, p2) == result
