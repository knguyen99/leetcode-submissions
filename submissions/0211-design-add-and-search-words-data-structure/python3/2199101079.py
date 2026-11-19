class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.start = Node()

    def addWord(self, word: str) -> None:
        curr = self.start
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.is_end = True

    def search_node(self, node, ptr, word):
        while ptr < len(word):
            if word[ptr] == ".":
                if not len(node.children):
                    return False
                for child in node.children:
                    if self.search_node(node.children[child], ptr+1, word):
                        return True
                return False
            elif word[ptr] not in node.children:
                return False
            node = node.children[word[ptr]]
            ptr += 1
        return node.is_end

    def search(self, word: str) -> bool:
        return self.search_node(self.start, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)