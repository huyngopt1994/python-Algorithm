# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/?fbclid=IwAR1qZJk2Sai4PNV4s_QCBBoWhe-pF0K9HL5ER-PkVdb1aEolwLDbPujnCgQ

class Node:
    def __init__(self):
        """We have count_word and child."""
        self.count_word = 0
        self.child = dict()


def add_word(root, s):
    tmp = root

    for ch in s:
        # loop for per character.
        if ch not in tmp.child:
            # check if ch is in current childs or not
            tmp.child[ch] = Node()
        # update tmp again
        tmp = tmp.child[ch]
        # update path with max weight:


def search_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return -1
        tmp = tmp.child[ch]
    # this final , just make sure we have any child or not
    if tmp.child:
        return 1
    else:
        return -1


if __name__ == '__main__':
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        added_words = int(input())

        root = Node()
        my_checked = []
        for _ in range(added_words):
            word = input()
            add_word(root=root, s=word)
            my_checked.append(word)
        is_good = True
        for word in my_checked:
            if search_word(root, word) == 1:
                # if this word
                is_good = False
                break
        if is_good:
            print('YES')
        else:
            print('NO')
