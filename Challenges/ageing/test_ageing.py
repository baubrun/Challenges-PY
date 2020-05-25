import pytest
from ageing import ageing


@pytest.mark.parametrize("x, n, result",

                         [
                             ({
                                 "Joel": 32,
                                 "Fred": 44,
                                 "Reginald": 65,
                                 "Susan": 33,
                                 "Julian": 13
                             },
                                 1,
                                 {"Joel": 33,
                                  "Fred": 45,
                                  "Reginald": 66,
                                  "Susan": 34,
                                  "Julian": 14}),
                             ({
                                 "Baby": 2,
                                 "Child": 8,
                                 "Teenager": 15,
                                 "Adult": 25,
                                 "Elderly": 71
                             }, 19, {
                                 "Baby": 21,
                                 "Child": 27,
                                 "Teenager": 34,
                                 "Adult": 44,
                                 "Elderly": 90
                             })
                         ]
                         )
def test_ageing(x, n, result):
    assert ageing(x, n) == result



@pytest.mark.parametrize("x, n, result",

                         [
                             ({
                                 "Joel": 322,
                                 "Fred": 424,
                                 "Reginald": 625,
                                 "Susan": 323,
                                 "Julian": 123
                             },
                                 1,
                                 {"Joel": 44,
                                  "Fred": 46,
                                  "Reginald": 456,
                                  "Susan": 354,
                                  "Julian": 124}),
                             ({
                                 "Baby": 29,
                                 "Child": 80,
                                 "Teenager": 105,
                                 "Adult": 225,
                                 "Elderly": 0
                             }, 19, {
                                 "Baby": 25,
                                 "Child": 257,
                                 "Teenager": 657,
                                 "Adult": 944,
                                 "Elderly": 909
                             })
                         ]
                         )
def test_ageing_neq(x, n, result):
    assert ageing(x, n) != result
