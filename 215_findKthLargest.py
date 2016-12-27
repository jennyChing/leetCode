class Solution(object):
    def recursiveFindKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0] # pick left most as the pivot element
        # bigger value goes to the left, smaller ones to the right
        left = [l for l in nums if l > pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r < pivot]
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k - len(left) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest(right, k - len(left) - len(equal))

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left


if __name__ == '__main__':
    nums = [3,2,11,5,6,4]
    nums = [2, 1]
    nums = [3,1,2,4]
    nums = [-1,2,0]
    nums = [7,6,5,4,3,2,1]
    k = 5
    res = Solution().findKthLargest(nums, k)
    print(res)
