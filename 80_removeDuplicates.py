class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        a, b, curr = 0, 0, nums[0]
        for n in nums[1:]:
            if n != curr:
                a += 1
                b = a
                curr = n
            else:
                a += 1
            print(a, b, curr)
            if a - b > 1:
                nums.remove(n)
        print(nums)
        return nums
if __name__ == '__main__':
    nums = [1, 2, 2, 2]
    res = Solution().removeDuplicates(nums)
    print(res)
