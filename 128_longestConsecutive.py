'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
# idea: union find
class SetNode(object):
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.rank = 1

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_parent(node):
            if node.parent == node:
                return node
            find_parent(node.parent)

        def update_parent(oldParent, newParent):
            for k, v in union_set.items():
                if v.parent == oldParent:
                    v.parent = newParent
                    newParent.rank += 1

        union_set, maxLen = {}, 0
        for n in nums:
            node = SetNode(n)
            node.parent = node
            if n + 1 in union_set and n - 1 in union_set: # combine groups
                plusOne, minusOne = find_parent(union_set[n + 1]), find_parent(union_set[n - 1])
                update_parent(plusOne, minusOne)
                node.parent = minusOne
                node.parent.rank += 1
            elif n + 1 in union_set:
                node.parent = node # n is new head of this group
                node.rank = union_set[n + 1].rank + 1 # lengh increase 1
                update_parent(union_set[n + 1], node)
            elif n - 1 in union_set:
                node.parent = find_parent(union_set[n - 1]) # tail of set
                node.parent.rank += 1
            union_set[n] = node
            maxLen = max(maxLen, node.parent.rank)
        return maxLen

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        union, maxL = {}, 0
        for n in nums:
            if n in union:
                continue
            start = end = n
            if n + 1 in union:
                end = union[n + 1][1]
            if n - 1 in union:
                start = union[n - 1][0]
            union[start] = union[end] = union[n] = (start, end)
            maxL = max(maxL, end - start + 1)
            print(union)
        return maxL

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    res = Solution().longestConsecutive(nums)
    print(res)

