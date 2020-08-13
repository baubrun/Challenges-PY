import pytest
from switching_pencils import color_pattern_times


@pytest.mark.parametrize("colors, result",
                         [

                    (["Blue"], 2),
                    (["Blue", "Blue", "Blue", "Red", "Red", "Red"], 13),
                    (["Red", "Yellow", "Green", "Blue"], 11)
                         ]

                         )
def test_color_pattern_times(colors, result):
    assert color_pattern_times(colors) == result








