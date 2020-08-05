import pytest
from thrones_1 import gameOfThrones



@pytest.mark.parametrize("letters, result",
                         [
                             ("cdefghmnopqrstuvw","NO"),
                             ("aaabbbb", "YES"),
                             ("cdcdcdcdeeeef", "YES")
                         ]

                         )
def test_strangeCounter(letters, result):
    assert gameOfThrones(letters) == result