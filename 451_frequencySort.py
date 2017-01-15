'''
451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
from heapq import heappush, heappop, heapreplace, heapify
import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # build a max heap to store tuple(freq, char)
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        h = [(-1 * v, k) for k, v in count.items()]
        heapify(h)
        res = ""
        while h:
            freq, char = heappop(h)
            res += char * -freq
        return res

if __name__ == "__main__":
    s = "tree"
    res = Solution().frequencySort(s)
    print(res)
