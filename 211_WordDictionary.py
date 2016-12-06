'''
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''
class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.memo = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def __directed_search(word, curr):
            if curr is None:
                return False
            if len(word) == 0:
                return curr.isWord
            if word[0] == '.':
                for k, v in curr.memo.items():
                    if __directed_search(word[1:], v) == True:
                        return True
                return False
            if word[0] not in curr.memo:
                return False
            else:
                return __directed_search(word[1:], curr.memo[word[0]])

        curr = self.root
        return __directed_search(word, curr)


if __name__ == "__main__":
        t = WordDictionary()
        t.addWord("ten")
        print(t.search("ten"))
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
