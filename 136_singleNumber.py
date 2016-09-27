class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_n = set()
        for n in nums:
            if n not in set_n:
                set_n.add(n)
            else:
                set_n.discard(n)
        arr_n = list(set_n)
        return arr_n[0]


