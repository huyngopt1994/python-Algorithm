# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/?fbclid=IwAR1qZJk2Sai4PNV4s_QCBBoWhe-pF0K9HL5ER-PkVdb1aEolwLDbPujnCgQ

class Node:
    def __init__(self):
        """We have count_word and child."""
        self.count_word = 0
        self.child = dict()
        self.weight = 0


def add_word(root, s, weight):
    tmp = root
    for ch in s:
        # loop for per character.
        if ch not in tmp.child:
            # check if ch is in current childs or not
            tmp.child[ch] = Node()
        # update tmp again
        tmp = tmp.child[ch]
        # update path with max weight:
        tmp.weight = max(tmp.weight, weight)

    tmp.weight = weight


def search_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return -1
        tmp = tmp.child[ch]
    return tmp.weight


if __name__ == '__main__':
    added_words, words_to_search = list(map(int, input().split()))
    root = Node()
    for _ in range(added_words):
        word, weight = input().split()
        weight = int(weight)
        add_word(root=root, s=word, weight=weight)

    for _ in range(words_to_search):
        word = input()
        result = search_word(root=root, s=word)
        print(result)
