class Solution(object):
    def missingNumber(self, nums):
        sort_list = [x for x in range(len(nums) + 1)]
        print(sort_list)
        for n in nums:
            sort_list.remove(n)
        return sort_list[0]
if __name__ ==  '__main__':
    res = Solution().missingNumber([0, 3, 2])
    print(res)
