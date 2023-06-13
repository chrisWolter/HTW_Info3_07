import subprocess
from decimal import Decimal 

"""
this helper methods make it easy to 
test a command line tool, and
the GradingScale class in particular.
"""

# helper methods

def call_shell_command(command_with_parameter, interactive_input):
    """
    calls a shell command and returns the output as string
    command_with_parameter: "java GradingScale"
    interactive_input: array with inputlines
    """
    interactive_input = [str(e) for e in interactive_input]
    interactive_input = '\n'.join(interactive_input) + '\n'
    interactive_input = interactive_input.encode("utf-8")
    command = command_with_parameter.split()
    output = subprocess.run(command, input = interactive_input, capture_output=True)
    return output.stdout.decode("utf-8").split('\n')

def call_grading_scale(input_values):
    command = "java GradingScale"
    input_values.append(-1)
    inputstrings = [str(i) for i in input_values]
    
    output = call_shell_command(command, inputstrings)
    # output:
    # ['Enter your numeric grades as percentages one per line  and end with a negative number:', 'Letter grade: A', 'Average: 50.0', '']
    grades = output[1:-1]
    average_str = grades.pop()# 'Average: 50.0'
    average_str = average_str.split().pop() # ['Average:', '50.0'], '50.0'
    average = Decimal(average_str)
    grades = [s.replace('Letter grade: ', '') for s in grades]
    return grades, average

def split_pairs(pairs_list):
    heads = [t[0] for t in pairs_list]
    tails = [t[1] for t in pairs_list]
    return heads, tails
