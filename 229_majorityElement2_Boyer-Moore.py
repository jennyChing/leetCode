'''
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
# use Boyer-Moore Majority Vote algorithm
        cnt1, cnt2, candidate1, candidate2 = 0, 0, 0, 1 # c1, c2 initially can't be same!
        for n in nums:
            if candidate1 == n:
                cnt1 += 1
            elif candidate2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1, cnt1 = n, 1
            elif cnt2 == 0:
                candidate2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]

if __name__ == "__main__":
    nums = [1, 2, 3]
    nums = [1, 0, 1, 3, 1, 5, 1]
    nums = [2, 2, 1, 3]
    nums = [3, 3, 4]
    nums = [3, 2, 2]
    res = Solution().majorityElement(nums)
    print(res)
