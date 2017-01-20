'''
424. Longest Repeating Character Replacement

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''
import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = j = 0
        count = collections.defaultdict(int)
        for j in range(1, len(s) + 1):
            count[s[j - 1]] += 1 # count the elements in s[i:j]
            most_com = count[max(count.keys(), key=lambda k: count[k])]
            if j - i - most_com > k: # check elements need to be replace <= k
                count[s[i]] -= 1
                i += 1
        return j - i

    def characterReplacement_refer(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = k + 1
        l, r = 0, 0
        counts = collections.Counter() # use most_common API
        for r in range(1, len(s) + 1): # right pointer
            counts[s[r - 1]] += 1
            print(counts)
            max_len = counts.most_common(1)[0][1]
            print(max_len)
            if r - l - max_len > k:
                counts[s[l]] -= 1 # out of k window, count of l decrease by 1
                l += 1 # left pointer
                print(r, l, counts, max_len, s[l:r])
            print("l:", l, "r:", r, s[l:r])
        return r - l

if __name__ == "__main__":
    s = "ABAB"
    k = 2
    s = "AABABBA"
    k = 1
    res = Solution().characterReplacement(s, k)
    print(res)
