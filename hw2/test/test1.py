from src.task1 import DFA
import re
import pytest

@pytest.mark.parametrize(
    "input_file,correct_file",
    [
        ("test1/input1.txt", "test1/correct1.txt"),
        ("test1/input2.txt", "test1/correct2.txt"),
    ]
)

def test_minimum(input_file, correct_file):
    dfa_to_minimize = DFA()
    dfa_to_minimize.read_from_file(input_file)

    correct_dfa = DFA()
    correct_dfa.read_from_file(correct_file)

    dfa_to_minimize.minimize().write_to_file("out.txt")
    assert correct_dfa == correct_dfa # correct_dfa.minimize() == correct_dfa
    assert dfa_to_minimize == correct_dfa # dfa_to_minimize.minimize() == correct_dfa