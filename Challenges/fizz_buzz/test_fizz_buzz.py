import pytest
from fizz_buzz import fizz_buzz


@pytest.mark.parametrize("x, result",
                         [
                             (10, [1, 2, 'Fizz', 4, 'Buzz',
                                   'Fizz', 7, 8, 'Fizz', 'Buzz']),
                             (15, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                                   'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']),
                             (1, [1])
                         ]
                         )
def test_fizz_buzz(x, result):
    assert fizz_buzz(x) == result


