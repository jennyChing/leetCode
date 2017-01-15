'''
456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
# O(n^2) time, too slow
        if nums == []:
            return False
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < stack[-1]: # found peak
                peak, right = stack[-1], nums[i]
                for n in nums[i:]:
                    if n < peak:
                        right = max(right, n)
                while stack and right <= stack[-1]:
                    stack.pop()
                if stack and stack[-1] < right:
                    return True
            stack.append(nums[i]) # not peak, add to stack
        return False

# O(n) time, refer ppl's solution
    def find132pattern_refer(self, nums):
        if len(nums) < 3:
            return False
        right, stack = float('-inf'), [nums[-1]]
        for i in range(len(nums) - 2, -1, -1): # loop from back to find right
            if nums[i] < right:
                return True
            if nums[i] > stack[-1]: # reach peak, pop stack and update right!
                while stack and nums[i] > stack[-1]:
                    right = max(stack.pop(), right)
                print("update right")
            stack.append(nums[i])
            print("curr:", nums[i], "right:", right, stack)
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 2]
    nums = [3, 5, 0, 3, 4]
    res = Solution().find132pattern_refer(nums)
    print(res)
