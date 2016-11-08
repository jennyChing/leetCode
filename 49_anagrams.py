'''
49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
# Data structure: hashtables using sorted s as key
        ana = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in ana:
                ana[sorted_s].append(s)
            else:
                ana[sorted_s] = [s]
        print(ana)

        return [v for k, v in ana.items()]

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    print(res)

