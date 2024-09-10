from .task1 import work
import re
import pytest

@pytest.mark.parametrize(
    "pattern,input_file,words",
    [
        ("ab.*", "input1.txt", ["abdswfdfdhsldasflkj", "fjhdfkjfdfsa", "ababab", "ab"]),
        ("ab.*ab", "input2.txt", ["abababasbdajaflkdab", "absdkdjd", "sjhsfhaasddfskab"]),
        ("ab.ab", "input3.txt", ["abaadwfsafa", "abdab", "abab"])
    ],
)
def test_regex(pattern: str, input_file: str, words: list[str]):
    for word in words:
        word_int = [ord(i) - ord('a') for i in word]
        
        result: bool = True
        if re.fullmatch(pattern, word) is None:
            result = False
        # print(word, result, work(input_file, word_int))
        # print(work(input_file, word_int))
        assert(result == work(input_file, word_int))
