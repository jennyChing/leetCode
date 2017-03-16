import collections
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        memo1, memo2 = collections.Counter(nums1), collections.Counter(nums2)
        res = []
        for k, v in memo1:
            if k in memo2:
                res.append(k)
        return res
