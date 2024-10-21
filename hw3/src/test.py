import pytest
import sys
import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

from task import Instruction, get_list_of_commands, check_string


@pytest.mark.parametrize(
    "regex,correct_list",
    [
        (
            "a+b+",
            [
                Instruction("char", "a"),
                Instruction(
                    "split",
                    (
                        0,
                        2,
                    ),
                ),
                Instruction("char", "b"),
                Instruction(
                    "split",
                    (
                        2,
                        4,
                    ),
                ),
                Instruction("match", None),
            ],
        ),
        (
            "a|(b|c)",
            [
                Instruction("split", (1, 3)),
                Instruction("char", "a"),
                Instruction("jmp", 7),
                Instruction("split", (4, 6)),
                Instruction("char", "b"),
                Instruction("jmp", 7),
                Instruction("char", "c"),
                Instruction("match", None),
            ],
        ),
        (
            "(a|b)+|a?a+",
            [
                Instruction("split", (1, 7)),
                Instruction("split", (2, 4)),
                Instruction("char", "a"),
                Instruction("jmp", 5),
                Instruction("char", "b"),
                Instruction("split", (1, 6)),
                Instruction("jmp", 11),
                Instruction("split", (8, 9)),
                Instruction("char", "a"),
                Instruction("char", "a"),
                Instruction("split", (9, 11)),
                Instruction("match", None),
            ],
        ),
    ],
)
def test_converter(regex: str, correct_list: list[Instruction]):
    for i in get_list_of_commands(regex):
        print(i.line, i.command)
    assert correct_list == get_list_of_commands(regex)


@pytest.mark.parametrize(
    "regex,words,results",
    [
        (
            "a+b+",
            ["abababa", "aaaa", "bbb", "a", "b", "ab", "aaaabbbb"],
            [False, False, False, False, False, True, True],
        ),
        (
            "a|(b|c)",
            ["a", "b", "c", "ba", "ffs", "d", "abdbds"],
            [True, True, True, False, False, False, False],
        ),
        (
            "(a|b)+|c?d+",
            [
                "ababababab",
                "aaaaa",
                "bbbbb",
                "cdddd",
                "cccc",
                "cd",
                "d",
                "aababac",
                "cda",
                "aacdbdb",
            ],
            [True, True, True, True, False, True, True, False, False, False],
        ),
    ],
)
def test_acceptor(regex: str, words: list[int], results: list[bool]):
    instruction_list = get_list_of_commands(regex)

    for word, res in zip(words, results):
        print(word, regex, res)
        assert res == check_string(word, 0, instruction_list, 0)
