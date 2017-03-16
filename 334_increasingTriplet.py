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

'''
refer better solution:
(1) Find the first smallest number in the 3 subsequence
(2) Find the second one greater than the first element, reset the first one if it's smaller
'''
    def increasingTriplet(nums):
	first = second = float('inf')
	for n in nums:
            if n <= first:
		first = n
	    elif n <= second:
		second = n
	    else:
		return True
	return False

if __name__ == '__main__':
    nums = [2,1,5,0,3]
    res = Solution().increasingTriplet(nums)
    print(res)

