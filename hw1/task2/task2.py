from queue import Queue

class Node: 
    id: int
    moves: dict[int, list]
    is_term: bool


    def __init__(self, id: int, is_term: bool):
        self.id = id
        self.is_term = is_term
        self.moves = dict()


class NFA:
    def __init__(self):
        self.all_nodes = list()
        self.reversed_nodes = list()
        self.start_nodes = list()
        self.term_nodes = list()
        self.n = 0
        self.m = 0

    def read_from_file(self, input_file: str) -> None:
        with open(input_file, "r") as f:
            all_lines: list[str] = f.read().split('\n')

            self.n: int = int(all_lines[0])
            self.m: int = int(all_lines[1])

            start_indexes: list[int] = [int(i) for i in all_lines[2].split()]
            term_indexes: list[int] = [int(i) for i in all_lines[3].split()]

            self.all_nodes = [Node(i, False) for i in range(self.n)]
            self.reversed_nodes = [Node(i, False) for i in range(self.n)]

            for index in term_indexes:
                self.all_nodes[index].is_term = True


            for i in range(4, len(all_lines)):
                v, w, u = [int(i) for i in all_lines[i].split()]
                if w in self.all_nodes[v].moves:
                    self.all_nodes[v].moves[w].append(self.all_nodes[u])
                else:
                    self.all_nodes[v].moves[w] = [self.all_nodes[u]]
                
                if w in self.reversed_nodes[u].moves:
                    self.reversed_nodes[u].moves[w].append(self.reversed_nodes[v])
                else:
                    self.reversed_nodes[u].moves[w] = [self.reversed_nodes[v]]
                
            self.start_nodes = [self.all_nodes[i] for i in start_indexes]
            self.term_nodes = [self.all_nodes[i] for i in term_indexes]

    
    def delete_node(self, id: int) -> None:
        v: Node = self.all_nodes[id]

        for key, nodes in self.reversed_nodes[id].moves.items():
            for u in nodes:
                self.all_nodes[u.id].moves[key].remove(v)


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

    def add_move(self, v: int, u: int, w: int) -> None:
        self.all_nodes[v].moves[w] = self.all_nodes[u]


def dfs(v: Node, used: list[bool]):
    used[v.id] = True
    
    for nodes in v.moves.values():
        for node in nodes:
            if not used[node.id]:
                dfs(node, used)


def nfa_to_dfa(nfa: NFA) -> DFA:
    used_normal: list[bool] = [False for i in range(nfa.n)]
    used_reverse: list[bool] = [False for i in range(nfa.n)]

    for node in nfa.start_nodes:
        dfs(node, used_normal)

    for node in nfa.term_nodes:
        dfs(nfa.reversed_nodes[node.id], used_reverse)

    for i in range(nfa.n):
        if not used_normal[i] or not used_reverse[i]:
            nfa.delete_node(i)

    new_ids: dict[list, int] = dict()
    id_to_nodes: dict[int, frozenset] = dict()
    id: int = 0
    dfa: DFA = DFA()

    new_ids[frozenset(nfa.start_nodes)] = id
    id_to_nodes[id] = frozenset(nfa.start_nodes)

    id += 1

    dfa.all_nodes.append(Node(0, False))
    q = Queue()
    
    q.put(0)

    while not q.empty():
        node_id = q.get()

        for i in range(nfa.m):
            new_node = set()

            is_term: bool = False

            for old_node in id_to_nodes[node_id]:
                if i not in old_node.moves:
                    continue

                for v in old_node.moves[i]:
                    if v.is_term:
                        is_term = True
                    new_node.add(v)

            if len(new_node) == 0:
                continue
            
            new_node = frozenset(new_node)

            if new_node not in new_ids:
                new_ids[new_node] = id
                id_to_nodes[id] = new_node
                dfa.all_nodes.append(Node(id, is_term))
                dfa.add_move(node_id, id, i)
                q.put(id)
                id += 1
            else:
                dfa.add_move(node_id, new_ids[new_node], i)

    dfa.start_node = dfa.all_nodes[0]
    dfa.n = id
    dfa.m = nfa.m

    for node in nfa.start_nodes:
        if node.is_term:
            dfa.all_nodes[0].is_term = True

    for node in dfa.all_nodes:
        if node.is_term:
            dfa.term_nodes.append(node)

    return dfa

input_file = input()
output_file = input()

nfa = NFA()
nfa.read_from_file(input_file)
dfa = nfa_to_dfa(nfa)

dfa.write_to_file(output_file)

