"""Root class to build a Trie."""


class Node:
    def __init__(self):
        """We have count_word and child."""
        self.count_word = 0
        self.child = dict()
        self.weight = 0


def add_word(root, s, weight=1):
    tmp = root
    for ch in s:
        # loop for per character.
        if ch not in tmp.child:
            # check if ch is in current childs or not
            tmp.child[ch] = Node()
        # update tmp again
        tmp = tmp.child[ch]

    tmp.countword += 1
    tmp.weight = weight
