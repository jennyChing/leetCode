class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uni_set = set()
        for n in nums:
            if n in uni_set:
                return True
            uni_set.add(n)
        return False

