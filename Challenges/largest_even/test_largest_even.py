import pytest
from largest_even import largest_even


@pytest.mark.parametrize("nums, result",
                         [
                             ([3, 7, 2, 1, 7, 9, 10, 13], 10),
                             ([1, 3, 5, 7], -1),
                            ([0, 19, 18973623], 0)
                         ]

                         )
def test_largest_even(nums, result):
    assert largest_even(nums) == result
