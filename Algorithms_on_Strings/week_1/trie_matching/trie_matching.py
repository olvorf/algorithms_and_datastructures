# python3

import sys
def build_trie(patterns):
    tree = {}
    new_node = 0
    for patterns in patterns:
        current_node = 0
        for i in range(len(patterns)):
            current_symbol = patterns[i]
            if tree.__contains__(current_node) and tree[current_node].__contains__(current_symbol):
                current_node = tree[current_node].get(current_symbol)
            else:
                new_node += 1
                if not tree.__contains__(current_node):
                    tree[current_node] = {}
                    tree[current_node][current_symbol] = new_node
                else:
                    tree[current_node][current_symbol] = new_node
                current_node = new_node
    return tree


def prefix_trie_matching(text, trie):
	v= 0
	for i in range(len(text)):
		symbol = text[i]
		if trie[v].__contains__(symbol):
			v = trie[v][symbol]
			if not trie.__contains__(v):
				return True
		else:
			return False

def trie_matching(text, trie):
	positions = []
	for i in range(len(text)):
		match = prefix_trie_matching(text[i:],trie)
		if match:
			positions.append(i)
	return positions


if __name__ == '__main__':
    text = input()
    n_patterns = int(input())
    patterns = list(input() for _ in range(n_patterns))
    tree = build_trie(patterns)
    positions = trie_matching(text, tree)
    for pos in positions:
        print(pos, end=' ')
