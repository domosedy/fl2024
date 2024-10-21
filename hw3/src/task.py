from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class Instruction:
    def __init__(self, command: str, line: None | int | tuple[int, int] | str = None):
        self.command = command
        self.line = line

    def __eq__(self, other):
        return self.command == other.command and self.line == other.line


class VisitorInterp(ExprVisitor):
    def __add_indexes(
        self, list_of_commands: list[Instruction], value: int
    ) -> list[Instruction]:
        for command in list_of_commands:
            if command.command == "jmp":
                command.line += value
            elif command.command == "split":
                command.line = tuple(map(lambda x: x + value, command.line))

        return list_of_commands

    def visitStart(self, ctx):
        return self.visit(ctx.expr()) + [Instruction("match")]

    def visitCharExpr(self, ctx):
        return [Instruction("char", ctx.getText())]

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitConnectExpr(self, ctx):
        left_child = self.visit(ctx.getChild(0))
        right_child = self.visit(ctx.getChild(1))

        return left_child + self.__add_indexes(right_child, len(left_child))

    def visitOrExpr(self, ctx):
        left_child = self.visit(ctx.left)
        right_child = self.visit(ctx.right)

        len_of_left = len(left_child)
        len_of_right = len(right_child)

        result_list = [Instruction("split", (1, 2 + len_of_left))]
        result_list += self.__add_indexes(left_child, 1)
        result_list.append(Instruction("jmp", 2 + len_of_left + len_of_right))
        result_list += self.__add_indexes(right_child, len(result_list))

        return result_list

    def visitAskExpr(self, ctx):
        child = self.visit(ctx.getChild(0))
        result_list = [Instruction("split", (1, 1 + len(child)))]

        result_list += self.__add_indexes(child, 1)
        return result_list

    def visitPlusExpr(self, ctx):
        result_list = self.visit(ctx.getChild(0))
        result_list.append(Instruction("split", (0, len(result_list) + 1)))

        return result_list

    def visitStarExpr(self, ctx):
        child = self.visit(ctx.getChild(0))

        result_list = [Instruction("split", (1, 2 + len(child)))]
        result_list += self.__add_indexes(child, 1)

        result_list.append(Instruction("jmp", 0))

        return result_list


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


def get_list_of_commands(regular: str):
    stream = InputStream(regular)

    lexer = ExprLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.start()

    visitor = VisitorInterp()
    return visitor.visit(tree)


if __name__ == "__main__":
    regular = input()
    result = get_list_of_commands(regular)
    line = 0

    for i in result:
        print(line, i.command, i.line)
        line += 1

    print(check_string(input(), 0, result, 0))
