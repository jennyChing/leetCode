from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        #for i in range(len(nums)):
        #    # this is using O(n^3)!
        #    product = reduce( (lambda x, y: x * y), nums[:i] + nums[i + 1:])
        #    res.append(product)

        # [O(n) Idea] calculate two arrays, one contains all multiple of all nums after i, and one for all nums before i. Then multiple the two arrays
        back, front = [1], [1]
        n = len(nums)
        curr = 1
        for i in range(n - 1, 0, -1):
            curr *= nums[i]
            back.append(curr)
        curr = 1
        for i in range(n - 1):
            curr *= nums[i]
            front.append(curr)
        print(front, back)
        for i in range(n):
            res.append(front[i] * back[n - i - 1])
        return res
if __name__ == "__main__":
    nums = [1,2,3,4]
    nums = [9,0,-2]
    nums = [2,3,5,0]
    res = Solution().productExceptSelf(nums)
    print(res)

