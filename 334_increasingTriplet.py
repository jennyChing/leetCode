'''
334. Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array. (no need to be continuous)

(simillar to #300 Longest Increasing Sequence)
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        potential = [float('inf')] * 3
        for n in nums:
            # n replace the first smallest element
            if n < potential[0]:
                potential[0] = n
            # n replace the second smallest element
            elif n < potential[1]:
                potential[1] = n
            else:
            # n is bigger then both first and second smallest element
                potential[2] = n
            if potential[2] != float('inf'):
                return True
            print(potential)
        return False
if __name__ == '__main__':
    nums = [2,1,5,0,3]
    res = Solution().increasingTriplet(nums)
    print(res)

