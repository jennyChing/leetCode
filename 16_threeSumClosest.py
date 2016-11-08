'''
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        threeSums = nums[:3]
        spread = abs(target - sum(threeSums))
        print(target)
        if spread == 0:
            return sum(threeSums)
        for i in range(3, len(nums)):
            if abs(target + nums[i] - min(threeSums)) < spread:
                print(spread, nums[i] - min(threeSums))
                threeSums.remove(min(threeSums))
                threeSums.append(nums[i])
                print("Remove min :", spread, nums[i], min(threeSums))
                print(threeSums)

            elif abs(target + nums[i] - max(threeSums)) < spread:
                threeSums.remove(max(threeSums))
                threeSums.append(nums[i])
                print("Remove max :", threeSums)
        return sum(threeSums)

if __name__ == "__main__":
    t1 = [1, 1, 1, 0]
    t1 = [0, 2, 1, -3]
    res = Solution().threeSumClosest(t1, 1)
    print(res)
