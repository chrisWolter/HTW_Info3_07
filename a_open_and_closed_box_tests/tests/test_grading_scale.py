from _decimal import Decimal

import pytest
import tests.test_helper as th

# your turn!
def test_a_f():
    input_values = [100, 89, 74, 59, 49]
    grades, average = th.call_grading_scale(input_values)
    assert grades == ['A', 'B', 'C', 'D', 'F']

@pytest.mark.xfail(reason="50 should be D not F")
def test_borders():
    input_values = [100, 90, 89, 75, 74, 60, 59, 50, 49, 0]
    grades, average = th.call_grading_scale(input_values)
    assert grades == ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'F', 'F']

@pytest.mark.xfail(reason="Average is divided by n + 1 and is therefor not correct")
def test_average():
    input_values = [10, 10, 10]
    grades, average = th.call_grading_scale(input_values)
    assert average == Decimal('10')