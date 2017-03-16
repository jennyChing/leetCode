class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        major = sorted(count.items(), key=lambda x: x[1])
        return major[-1][0]


