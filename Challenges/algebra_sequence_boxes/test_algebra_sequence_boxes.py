import pytest
from alegra_sequence_boxes import box_seq


@pytest.mark.parametrize("x, result",
                         [(0, 0), (1, 3), (2, 2)]
                         )
def test_box_seq(x, result):
    assert box_seq(x) == result



@pytest.mark.parametrize("x, result",
                         [(0, 99), (78, 45), (3, 4561)]
                         )
def test_box_seq_neq(x, result):
    assert box_seq(x) != result



