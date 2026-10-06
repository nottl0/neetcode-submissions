class Node:
    def __init__(self, val: str = None):
        self.val = val
        self.children = list()
        self.child_vals = dict()
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        prev = self.head
        for letter in word:
            if letter in prev.child_vals:
                node = prev.child_vals[letter]
            else:
                node = Node(val=letter)
                prev.children.append(node)
                prev.child_vals[letter] = node
            prev = node
        prev.is_end = True

    def search(self, word: str) -> bool:
        node = self.head
        def dfs(node, i):
            if i >= len(word):
                return node.is_end
            elif word[i] == ".":
                for n in node.children:
                    if dfs(n, i+1):
                        return True
                return False
            elif word[i] in node.child_vals:
                next_node = node.child_vals[word[i]]
                return dfs(next_node, i+1)
            else:
                return False
        return dfs(node, 0)
