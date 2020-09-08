import pytest
from missing_num import missing_num


@pytest.mark.parametrize("arr, result",
                         [

                    ([1, 2, 3, 4, 6, 7, 8, 9, 10], 5),
                    ([7, 2, 3, 6, 5, 9, 1, 4, 8], 10),
                    ([10, 5, 1, 2, 4, 6, 8, 3, 9], 7)
                         ]

                         )
def test_missing_num(arr, result):
    assert missing_num(arr) == result








