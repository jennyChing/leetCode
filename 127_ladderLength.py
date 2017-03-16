'''
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the word list
    For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
'''
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        graph = {}
        for w in wordList:
            for i in range(len(w)):
                s = w[:i] + "_" + w[i + 1:]
                graph[s] = graph.get(s, []) + [w]
        def __directed_bfs(beginWord):
            q, visited = collections.deque([(beginWord, 1)]), set()
            while q:
                word, steps = q.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == endWord:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neighbors = graph.get(s, [])
                        for n in neighbors:
                            if n not in visited:
                                q.append((n, steps + 1))
            return 0
        return __directed_bfs(beginWord)

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    res = Solution().ladderLength(beginWord, endWord, wordList)
    print(res)

