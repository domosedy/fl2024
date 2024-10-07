from queue import Queue
from typing import Self


class Node:
    id: int
    moves: dict[int, list[Self] | Self]
    is_term: bool

    def __init__(self, id: int, is_term: bool):
        self.id = id
        self.is_term = is_term
        self.moves = dict()


class DFA:
    def __init__(self):
        self.all_nodes = list()
        self.start_node = Node(0, False)
        self.term_nodes = list()
        self.n = 0
        self.m = 0

    def write_to_file(self, output_file: str) -> None:
        with open(output_file, "w") as f:
            print(self.n, file=f)
            print(self.m, file=f)
            print(self.start_node.id, file=f)

            print(*[node.id for node in self.term_nodes], file=f)

            for node in self.all_nodes:
                for key, connected_node in node.moves.items():
                    print(node.id, key, connected_node.id, file=f)

    def read_from_file(self, input_file: str) -> None:
        with open(input_file, "r") as f:
            all_lines: list[str] = f.read().split("\n")

            self.n: int = int(all_lines[0])
            self.m: int = int(all_lines[1])

            start_indexes: list[int] = [int(i) for i in all_lines[2].split()]
            term_indexes: list[int] = [int(i) for i in all_lines[3].split()]

            self.all_nodes = [Node(i, False) for i in range(self.n)]

            for index in term_indexes:
                self.all_nodes[index].is_term = True

            for i in range(4, len(all_lines)):
                v, w, u = [int(i) for i in all_lines[i].split()]
                self.all_nodes[v].moves[w] = self.all_nodes[u]

            self.start_node = self.all_nodes[start_indexes[0]]
            self.term_nodes = [self.all_nodes[i] for i in term_indexes]

    def __add_new_node(self) -> None:
        new_node: Node = Node(self.n, False)
        self.n += 1

        for letter in range(self.m):
            new_node.moves[letter] = new_node

        for node in self.all_nodes:
            for letter in range(self.m):
                if letter not in node.moves.keys():
                    node.moves[letter] = new_node

        self.all_nodes.append(new_node)

    def __get_reversed_nodes(self) -> list[Node]:
        list_of_nodes: list[Node] = [Node(i, False) for i in range(self.n)]

        for node in self.all_nodes:
            for letter in node.moves.keys():
                id_first = node.id
                id_second = node.moves[letter].id

                if letter not in list_of_nodes[id_second].moves.keys():
                    list_of_nodes[id_second].moves[letter] = []

                list_of_nodes[id_second].moves[letter].append(list_of_nodes[id_first])

        return list_of_nodes

    def __build_table(self) -> None:
        q = Queue()
        reversed_moves = self.__get_reversed_nodes()

        marked = [[False for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if (
                    not marked[i][j]
                    and self.all_nodes[i].is_term != self.all_nodes[j].is_term
                ):
                    marked[i][j] = marked[j][i] = True
                    q.put(
                        (
                            i,
                            j,
                        )
                    )

        while not q.empty():
            u, v = q.get()

            for letter in range(self.m):
                if (
                    letter not in reversed_moves[v].moves.keys()
                    or letter not in reversed_moves[u].moves.keys()
                ):
                    continue
                for prev_v in reversed_moves[v].moves[letter]:
                    for prev_u in reversed_moves[u].moves[letter]:
                        if not marked[prev_u.id][prev_v.id]:
                            marked[prev_u.id][prev_v.id] = marked[prev_v.id][
                                prev_u.id
                            ] = True
                            q.put(
                                (
                                    prev_u.id,
                                    prev_v.id,
                                )
                            )

        return marked

    def __build_from_components(
        self, components: list[int], components_count: int
    ) -> Self:
        list_of_all_nodes = [Node(i, False) for i in range(components_count)]
        start_node = list_of_all_nodes[0]
        term_nodes = []

        for i in range(self.n):
            if components[i] == -1:
                continue

            current_node = self.all_nodes[i]
            for letter, node in current_node.moves.items():
                list_of_all_nodes[components[i]].moves[letter] = list_of_all_nodes[
                    components[node.id]
                ]

            if current_node == self.start_node:
                start_node = list_of_all_nodes[components[i]]

            if current_node.is_term:
                list_of_all_nodes[components[i]].is_term = True

        for node in list_of_all_nodes:
            if node.is_term:
                term_nodes.append(node)

        dfa: Self = DFA()
        dfa.all_nodes = list_of_all_nodes
        dfa.term_nodes = term_nodes
        dfa.start_node = start_node
        dfa.n = components_count
        dfa.m = self.m

        return dfa

    def __get_reachable(self, v: Node, used: list[bool]) -> None:
        used[v.id] = True
        for node in v.moves.values():
            if not used[node.id]:
                self.__get_reachable(node, used)

    def minimize(self) -> Self:
        reachable = [False for i in range(self.n)]
        marked = self.__build_table()
        components = [-1 for i in range(self.n)]

        self.__get_reachable(self.start_node, reachable)

        components_count = 0
        for i in range(self.n):
            if not reachable[i]:
                continue

            if components[i] == -1:
                components[i] = components_count
                for j in range(i + 1, self.n):
                    if not marked[i][j]:
                        components[j] = components_count
                components_count += 1
        return self.__build_from_components(components, components_count)

    def __eq__(self, other: Self) -> bool:
        self_dfa = self.minimize()
        other_dfa = other

        if (
            self_dfa.n != other_dfa.n
            or self_dfa.m != other_dfa.m
            or len(self_dfa.term_nodes) != len(other_dfa.term_nodes)
        ):
            return False

        isomporhic_indexes = [-1] * self_dfa.n

        self_q = Queue()
        other_q = Queue()

        isomporhic_indexes[other_dfa.start_node.id] = self_dfa.start_node.id

        self_q.put(self_dfa.start_node)
        other_q.put(other_dfa.start_node)

        while not self_q.empty() and not other_q.empty():
            u = self_q.get()
            v = other_q.get()

            if u.moves.keys() != v.moves.keys():
                return False

            for letter in u.moves.keys():
                new_u = u.moves[letter]
                new_v = v.moves[letter]

                prev_index, isomporhic_indexes[new_v.id] = (
                    isomporhic_indexes[new_v.id],
                    new_u.id,
                )

                if prev_index != -1 and prev_index != new_u.id:
                    return False
                elif prev_index != -1:
                    continue

                self_q.put(new_u)
                other_q.put(new_v)

        if self_q.empty() != other_q.empty():
            return False

        for i in range(self_dfa.n):
            state_from_other = other_dfa.all_nodes[i]
            state_from_self = self_dfa.all_nodes[isomporhic_indexes[i]]

            if state_from_other.moves.keys() != state_from_self.moves.keys():
                new_state_other = state_from_other.moves[letter]
                new_state_self = state_from_self.moves[letter]

                if isomporhic_indexes[new_state_other.id] != new_state_self.id:
                    return False

        return True

    def accepts(self, s: str) -> bool:
        old_states: set[Node] = set(self.start_node)
        new_states: set[Node] = set()

        for letter in s:
            for state in old_states:
                if letter in state.moves.keys():
                    for new_node in state.moves[letter]:
                        new_states.add(new_node)
            old_states.clear()
            old_states, new_states = new_states, old_states

        return any(lambda x: x.is_term, old_states)


if __name__ == "__main__":
    input_file = "test/test1/input1.txt"
    output_file = "out.txt"

    dfa = DFA()

    dfa.read_from_file(input_file)
    new_dfa = dfa.minimize()

    new_dfa.write_to_file(output_file)
