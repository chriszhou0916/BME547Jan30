@pytest.mark.parameterize('a,b,expected',[
(2,3,5),
(5.-2.3),
(10,20,30)
])
# this is a decorator. runs this test multiple times with different inputs
def test_calculator():
    from calculator import add_two_numbers
    answer = add_two_numbers(2,3)
    assert answer == 5
