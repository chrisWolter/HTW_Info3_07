from a_open_and_closed_box_tests.python.absolute import absolute_value_of

def test_positive():
    assert absolute_value_of(6) == 6

def test_negative():
    assert absolute_value_of(-6) == 6

def test_positive_with_comma():
    assert absolute_value_of(6.3) == 6.3

def test_negative_with_comma():
    assert absolute_value_of(-6.3) == 6.3
