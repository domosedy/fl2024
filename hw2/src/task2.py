from typing import Optional


class Instruction:

    def __init__(self, command: str, line: None | int | tuple[int, int] | str = None):
        self.command = command
        self.line = line

    def __eq__(self, other):
        return self.command == other.command and self.line == other.line


def parse_regular_expression(
    regstr: str, is_recursive: bool = False
) -> list[Instruction]:
    instruction_list: list[Instruction] = []
    current_index = 0

    i = 0

    if "|" in regstr:
        previous_or = 0
        while i < len(regstr):
            if regstr[i] == "|":
                previous_or = i
                break
            i += 1

        first_half = parse_regular_expression(regstr[0:previous_or], True)
        print(regstr[0:previous_or])

        second_half = parse_regular_expression(
            regstr[previous_or + 1 : len(regstr)], True
        )

        current_index = 1
        instruction_list.append(
            Instruction("split", (current_index, current_index + len(first_half) + 1))
        )
        for command in first_half:
            if command.command == "jmp":
                command.line += current_index
            elif command.command == "split":
                line1, line2 = command.line
                command.line = (line1 + current_index, line2 + current_index)

        instruction_list += first_half
        instruction_list.append(
            Instruction("jmp", len(instruction_list) + len(second_half) + 1)
        )

        current_index = len(instruction_list)
        for command in second_half:
            if command.command == "jmp":
                command.line += current_index
            elif command.command == "split":
                line1, line2 = command.line
                command.line = (line1 + current_index, line2 + current_index)

        instruction_list += second_half

        if not is_recursive:
            instruction_list.append(Instruction("match"))

        return instruction_list

    regstr += "#"
    while i + 1 < len(regstr):
        if regstr[i + 1] == "?":
            instruction_list.append(Instruction("char", regstr[i]))
            instruction_list.append(
                Instruction("split", (current_index, current_index + 2))
            )
            current_index += 2
            i += 2
            continue

        if regstr[i + 1] == "*":
            instruction_list.append(
                Instruction("split", (current_index + 1, current_index + 3))
            )
            instruction_list.append(Instruction("char", regstr[i]))
            instruction_list.append(Instruction("jmp", current_index))
            current_index += 3
            i += 2
            continue

        if regstr[i + 1] == "+":
            instruction_list.append(Instruction("char", regstr[i]))
            current_index += 1
            instruction_list.append(
                Instruction("split", (current_index - 1, current_index + 1))
            )
            current_index += 1
            i += 2
            continue

        instruction_list.append(Instruction("char", regstr[i]))
        i += 1
        current_index += 1

    if not is_recursive:
        instruction_list.append(Instruction("match"))

    return instruction_list


def check_string(
    word: str,
    current_index: int,
    instruction_list: list[Instruction],
    instruction_pointer: int,
) -> bool:
    if instruction_list[instruction_pointer].command == "match":
        return current_index == len(word)

    current_instruction = instruction_list[instruction_pointer]

    if current_instruction.command == "char":
        if (
            current_index >= len(word)
            or word[current_index] != current_instruction.line
        ):
            return False

        return check_string(
            word, current_index + 1, instruction_list, instruction_pointer + 1
        )

    if current_instruction.command == "jmp":
        return check_string(
            word, current_index, instruction_list, current_instruction.line
        )

    line1, line2 = current_instruction.line
    return check_string(word, current_index, instruction_list, line2) or check_string(
        word, current_index, instruction_list, line1
    )


if __name__ == "__main__":
    regex = input()
    instruction_list = parse_regular_expression(regex)

    j = 0
    for i in instruction_list:
        print(j, i.command, i.line)
        j += 1

    word = input()
    print(check_string(word, 0, instruction_list, 0))
