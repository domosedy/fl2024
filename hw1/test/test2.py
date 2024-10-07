import pytest
from solution.task1 import work
from solution.task2 import work as work_test2

@pytest.mark.parametrize(
    "input_file,words",
    [
        ("test2/input3.txt", ["ababaabababasbadsbfajlafhab", "lfasjlfkalsdjf", "aba", "ab", "ababab", "abdeab"])
    ]
)
def test_converter(input_file: str, words: list[int]):
    work_test2(input_file, "output.txt")

    for word in words:
        word_int = [ord(i) - ord('a') for i in word]

        result = work(input_file, word_int)
        assert(result == work("output.txt", word_int))