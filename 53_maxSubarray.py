'''
Kadane algorithm
'''
class Solution(object):
    def maxSubArray(self, nums):
        max_so_far, max_end_here, less_neg = 0, 0, float('-inf')
        isAllNeg = True
        for n in nums:
            max_end_here += n
            #print(less_neg)
            if n <= 0:
                less_neg = max(less_neg, n)
            if max_end_here < 0:
                max_end_here = 0
            if max_end_here > max_so_far: # update max_so_far
                isAllNeg = False
                #print(n, max_end_here, max_so_far)
                max_so_far = max_end_here
        if isAllNeg == True:
            return less_neg
        return max_so_far
if __name__ == '__main__':
    nums = [-2]
    res = Solution().maxSubArray(nums)
    print(res)


