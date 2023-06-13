import pytest
import tests.test_helper as th
import re
# test examples
command_python = "python3 ../python/tax_time.py"
command_java = "java javasource.TaxTime"
command = command_python 

def test_example():
    input_values = [ 45000, 3 ]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [45000.0, 3.0, 8300.0, 300.0]

def extract_numbers(output):
    relevant_output = output[4:-2]
    numbers = [float(re.sub(r'.* ([0-9.]+).*',r'\1', s)) for s in relevant_output]
    return numbers

def test_example_with_string():
    input_values = [ 45000, 3 ]
    output = th.call_shell_command(command, input_values)
    relevant_output = output[4:-2]
    output_str = '\n'.join(output[4:-2])
    expected_str = """Your income was 45000.0 €.
You have 3 family members.
Your total tax is 8300.0 €.
Family member tax saving is 300 €."""
    assert output_str == expected_str

def test_wrong_income():
    input_values = ["A", 3]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == []

def test_income_negative():
    input_values = ["-1", 3]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == []

def test_wrong_familymebers():
    input_values = [200, "A"]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == []

def test_negative_familymebers():
    input_values = [200, 0]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == []

def test_income_below_10000():
    input_values = [9000, 1]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [9000.0, 1.0, 880.0, 100.0]

def test_income_below_50000():
    input_values = [49000, 1]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [49000.0, 1.0, 9460.0, 100.0]

def test_income_above_50000():
    input_values = [100000, 1]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [100000.0, 1.0, 19300.0, 100.0]

def test_tax_below_zero():
    input_values = [50, 1]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [50.0, 1.0, 0.0, 100.0]

def test_income_below_10000_three_family():
    input_values = [9000, 3]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [9000.0, 3.0, 680.0, 300.0]

def test_income_below_50000_three_family():
    input_values = [49000, 3]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [49000.0, 3.0, 9260.0, 300.0]

def test_income_aboce_50000_three_family():
    input_values = [100000, 3]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [100000.0, 3.0, 19100.0, 300.0]