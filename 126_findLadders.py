'''
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                graph[w[:i] + '_' + w[i + 1:]].append(w)

        currLevel = collections.deque([(beginWord, [])]) # bfs
        visited = set()
        res = []
        while currLevel: # bfs level traversal
            nextLevel = collections.deque([])
            currPaths = []
            while currLevel:
                w, partial = currLevel.popleft()
                if w not in visited:
                    if w == endWord:
                        currPaths.append(partial + [w])
                    for i in range(len(w)):
                        for n in graph[w[:i] + '_' + w[i + 1:]]:
                            if n not in visited:
                                currLevel.append((n, partial + [w]))
                                print(n, currLevel)
            visited.add(w)
            currLevel = nextLevel
            res = currPaths

        shortest = min(map(len, res))
        return [r for r in res if len(r) == shortest]

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hit", "hot","dot","dog","lot","log","cog"]
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    res = Solution().findLadders(beginWord, endWord, wordList)
    print(res)

