# test_*** file name tells Pytest to automatically recognize it
# start in home directory, then look in sub-directory
# will be able to find anything that starts with test_

from temp_conversion_module import convert_c_to_f, fever_detection
def test_convert_c_to_f():
    # Go to the file in the same folder, get that function over
# importing whole module vs specific function
# still need module name if importing whole module

    answer = convert_c_to_f(20)
    expected = 68
    assert answer == expected
    # assert is evaluated. if true, the test passes
def test2():
    answer = convert_c_to_f(-40)
    expected = -40
    assert answer == expected

def test3():
    answer = convert_c_to_f(50)
    expected = 122
    assert answer == expected

def test_fever_detection():
    temp_list = [93.0, 98, 100, 105, 101]
    max_temp, is_fever = fever_detection(temp_list)
    expected_max = 105
    expected_fever = True
    assert max_temp == expected_max
def test_fever_detection_bad():
    temp_list = [93.0, "98", 100, 105, 101]
    max_temp, is_fever = fever_detection(temp_list)
    expected_max = 105
    expected_fever = True
    assert max_temp == expected_max
