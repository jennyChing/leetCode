class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1_dic = {}
        n2_dic = {}
        for n in nums1:
            if n in n1_dic:
                n1_dic[n] += 1
            else:
                n1_dic[n] = 1
        for n in nums2:
            if n in n2_dic:
                n2_dic[n] += 1
            else:
                n2_dic[n] = 1
        inters = []
        for k, v in n1_dic.items():
            if k in n2_dic:
                cnt = min(n2_dic[k], v)
                for _ in range(cnt):
                    inters.append(k)
        return inters

import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        memo1, memo2 = collections.Counter(nums1), collections.Counter(nums2)
        res = []
        for k, v in memo1.items():
            if k in memo2:
                res += [k] * min(memo2[k], v)
        return res

