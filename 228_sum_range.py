'''
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        start = 0
        nums.append(float('inf'))
        for i, v in enumerate(nums):
            if i > 0 and v != nums[i - 1] + 1:
                partial = str(nums[start]) + "->" + str(nums[i - 1]) if start != i - 1 else str(nums[i - 1])
                res.append(partial)
                start = i
        return res

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    res = Solution().summaryRanges(nums)
    print(res)
