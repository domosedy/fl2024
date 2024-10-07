import pytest
from src.task2 import Instruction, parse_regular_expression, check_string


@pytest.mark.parametrize(
    "regex,correct_list",
    [
        (
            "a+b+",
            [
                Instruction("char", "a"),
                Instruction("split", (0, 2,)),
                Instruction("char", "b"),
                Instruction("split", (2, 4,)),
                Instruction("match"),
            ],
        ),
        (
            "a+b*|a?",
            [
                Instruction("split", (1, 7)),
                Instruction("char", "a"),
                Instruction("split", (1, 3)),
                Instruction("split", (4, 6)),
                Instruction("char", "b"),
                Instruction("jmp", 3),
                Instruction("jmp", 9),
                Instruction("char", "a"),
                Instruction("split", (7, 9)),
                Instruction("match", None),
            ],
        ),
    ],
)
def test_converter(regex: str, correct_list: list[Instruction]):
    assert correct_list == parse_regular_expression(regex)


@pytest.mark.parametrize(
    "regex,words,results",
    [
        (
            "a+b+",
            ["abababa", "aaaa", "bbb", "a", "b", "ab", "aaaabbbb"],
            [False, False, False, False, False, True, True],
        ),
        (
            "a+b*|a?",
            ["ababb", "bbb", "ab", "a", "bbb", "aba", "aaaa"],
            [False, False, True, True, False, False, True],
        ),
    ],
)
def test_acceptor(regex: str, words: list[int], results: list[bool]):
    instruction_list = parse_regular_expression(regex)

    for word, res in zip(words, results):
        print(word, regex, res)
        assert res == check_string(word, 0, instruction_list, 0)
