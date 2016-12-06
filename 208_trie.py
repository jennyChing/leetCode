'''
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.
'''
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo = {} # char: node location
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr.memo:
                curr.memo[c] = TrieNode()
            curr = curr.memo[c]
        curr.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr.memo:
                return False
            curr = curr.memo[c]
        return curr.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr.memo:
                return False
            curr = curr.memo[c]
        return True


if __name__ == "__main__":
        t = Trie()
        t.insert("ten")
        print(t.search("te"))
        print(t.search("ten"))
        print(t.startsWith("te"))
        print(t.startsWith("x"))
        t.insert("x")
        print(t.startsWith("x"))
# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
