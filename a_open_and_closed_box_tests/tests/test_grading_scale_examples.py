import tests.test_helper as th
import pytest
# test examples

def test_simple_example():
    input_values = [ 100, 80 ]
    grades, average = th.call_grading_scale(input_values)
    assert grades == ['A', 'B']

def test_average_is_returned_as_decimal():
    input_values = [ 100, 80 ]
    grades, average = th.call_grading_scale(input_values)
    assert str(type(average)) == "<class 'decimal.Decimal'>"

def test_test_helper_split_pairs():
    """
    using the split_pairs method above, input values and expected grades
    can be given as a list of tuples:
    """
    test_data = [(90, 'A'), (80, 'B')]
    input_values, expected_grades = th.split_pairs(test_data)
     
    assert input_values == [90, 80]
    assert expected_grades == ['A', 'B']
    

# https://docs.pytest.org/en/7.1.x/how-to/skipping.html
#   -r chars              Show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed, (p)assed, (P)assed with output, (a)ll except passed (p/P), or (A)ll.
#                         (w)arnings are enabled by default (see --disable-warnings), 'N' can be used to reset the list. (default: 'fE').

@pytest.mark.xfail(reason="Example how to mark a found bug")
def test_expect_fail():
    assert 1 == 2
