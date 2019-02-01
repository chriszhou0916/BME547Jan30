import pytest
@pytest.mark.parametrize('a,b,expected',[
(2,3,5),
(5,-2,3),
(10,20,30)
])
# this is a decorator. runs this test multiple times with different inputs
def test_calculator(a,b,expected):
    from calculator import add_two_numbers
    answer = add_two_numbers(a,b)
    assert answer == pytest.approx(expected)

@pytest.mark.parametrize('a,b,expected',[
(3,2,1),
(5,4,1)
])
def test_subtract(a,b,expected):
    from calculator import subtract_two_numbers
    assert subtract_two_numbers(a,b) == expected


@pytest.mark.parametrize('a,expected',[
([3,4,5],5),
([6,7,8],8)
])
def test_findmax(a,expected):
    from calculator import find_max
    assert find_max(a) == expected

@pytest.mark.parametrize('a,expected',[
([3,4,5],3),
([6,7,8],6)
])
def test_findmin(a,expected):
    from calculator import find_min
    assert find_min(a) == expected
