class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.child_vals = {}

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return 
        prev = self.head
        for letter in word:
            try:
                node = prev.child_vals[letter]
            except:
                node = Node(val=letter)
                prev.children.append(node)
                prev.child_vals[letter] = node
            prev = node
        prev.children.append(None)

    def search(self, word: str) -> bool:
        node = self.head
        for letter in word:
            if letter in node.child_vals:
                node = node.child_vals[letter]
            else:
                return False

        if None in node.children:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for letter in prefix:
            if letter in node.child_vals:
                node = node.child_vals[letter]
            else:
                return False
        return True
        