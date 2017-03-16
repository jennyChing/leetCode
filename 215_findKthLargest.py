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
        def partition(left, right):
            pivot_val = nums[right]
            pivot_idx = left
            for i in range(left, right):
                if nums[i] > pivot_val:
                    nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                    pivot_idx += 1
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            return pivot_idx

        left, right = 0, len(nums) - 1
        while left <= right:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            elif idx > k - 1:
                right = idx - 1
            else:
                left = idx + 1

if __name__ == '__main__':
    nums = [2, 1]
    nums = [3,1,2,4]
    nums = [-1,2,0]
    nums = [7,6,5,4,3,2,1]
    nums = [3,2,11,5,6,4]
    k = 5
    res = Solution().findKthLargest(nums, k)
    print(res)
