class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
	self.nums = nums
        self.prefixSum = []
        for i in range(len(nums)):
            if i == 0:
                self.prefixSum.append(nums[0])
            else:
                self.prefixSum.append(nums[i] + self.prefixSum[-1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum[j] - self.prefixSum[i - 1] if i > 0 else self.prefixSum[j]

# Your NumArray object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))

