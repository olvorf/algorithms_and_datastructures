# python3

import sys
def build_trie(patterns):
    trie = {}
    new_node = 0
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if trie.__contains__(current_node) and trie[current_node].__contains__(current_symbol):
                current_node = trie[current_node].get(current_symbol)
            else:
                new_node += 1
                if not trie.__contains__(current_node):
                    trie[current_node] = {}
                    trie[current_node][current_symbol] = new_node
                else:
                    trie[current_node][current_symbol] = new_node
                current_node = new_node
    return trie

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
