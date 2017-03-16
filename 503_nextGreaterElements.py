'''
503. Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
'''
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxE = max(nums)
        #  First we put all indexes into the stack, smaller index on the top
        stack = nums[::-1]
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == maxE:
                res[i] = -1
            elif stack and nums[i] < stack[-1]:
                res[i] = stack[-1]
            else:
                while stack and nums[i] >= stack[-1]:
                    stack.pop()
                res[i] = stack[-1]
            stack.append(nums[i])
            print(stack)
        return res
if __name__ == '__main__':
    nums = [6,1,3,1,2,3,5]
    nums = [5,4,3,2,1]
    res = Solution().nextGreaterElements(nums)
    print(res)

