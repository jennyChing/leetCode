class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.__data = nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        n = len(self.__data)
        return sum(self.__data[i: min(j + 1, n)])


# Your NumArray object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))

