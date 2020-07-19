import pytest
from lisas_workbook import workbook



@pytest.mark.parametrize("n, k, arr, result",

    [
      (5, 3, [4,2,6,1,10], 4)  
    ]

)
def test_workbook(n, k, arr, result):
    assert workbook(n, k, arr) == result