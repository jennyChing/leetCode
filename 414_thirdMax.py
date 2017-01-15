'''
414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# need distinct 3rd maximum!
        first = second = third = float('-inf')
        for n in nums:
            if n > first:
                first, second, third = n, first, third
            elif first > n > second:
                second, third = n, second
            elif second > n > third:
                third = n
            print(first, second, third)
        # Use 3 variable, Wrong Answer!! (if 3rd maximum is -inf)
        return third if third > float('-inf') else first

    def thirdMax_refer(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [float('-inf')] * 3
        for n in nums:
            if n not in v:
                if n > v[0]: v = [n, v[0], v[1]]
                elif n > v[1]: v = [v[0], n, v[1]]
                elif n > v[2]: v = [v[0], v[1], n]
            print(v, float('-inf') in v)
        return max(nums) if float('-inf') in v else v[2]


if __name__ == "__main__":
    nums = [3, 2, 1, 4]
    nums = [2, 2, 3, 1]
    nums = [1,2,2]
    nums = [1, float('-inf'), 2]
    res = Solution().thirdMax(nums)
    res = Solution().thirdMax_refer(nums)
    print(res)
