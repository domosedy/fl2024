class node: 
    id: int
    moves: dict[int, list]
    is_term: bool

    def __init__(self, id: int, is_term: bool):
        self.id = id
        self.is_term = is_term
        self.moves = dict()


def is_accepted(word: list[int], start_nodes: list[node]) -> bool:
    old_states: set[node] = set(start_nodes)
    new_states: set[node] = set()

    for letter in word:
        for state in old_states: 
            if letter in state.moves.keys():
                for new_state in state.moves[letter]: 
                    new_states.add(new_state)
        
        old_states.clear()
        old_states, new_states = new_states, old_states
    
    for state in old_states:
        if state.is_term:
            return True
        
    return False


def work(input_file: str, word: list[int]) -> bool:
    with open(input_file, "r") as f:
        all_lines: list[str] = f.read().split('\n')

        n: int = int(all_lines[0])
        m: int = int(all_lines[1])

        start_indexes: list[int] = [int(i) for i in all_lines[2].split()]
        term_indexes: list[int] = [int(i) for i in all_lines[3].split()]

        all_nodes: list[node] = [node(i, False) for i in range(n)]

        for index in term_indexes:
            all_nodes[index].is_term = True


        for i in range(4, len(all_lines)):

            if all_lines[i] == "":
                continue 
            v, w, u = [int(i) for i in all_lines[i].split()]
            if w in all_nodes[v].moves:
                all_nodes[v].moves[w].append(all_nodes[u])
            else:
                all_nodes[v].moves[w] = [all_nodes[u]]
            
        start_nodes: list[node] = [all_nodes[i] for i in start_indexes]
        # print(word)

        return is_accepted(word, start_nodes)
    
if __name__ == "__main__":
    input_file: str = input()
    word: list[int] = [int(i) for i in input().split()]

    print(work(input_file, word))