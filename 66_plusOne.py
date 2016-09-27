class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        i, carry = 0, 0
        a = digits[::-1]
        a[0] += 1
        while i < len(digits):
            if a[i] + carry > 9:
                res.append(a[i] + carry - 10)
                carry = 1
            else:
                res.append(a[i] + carry)
                carry = 0
            i += 1
        if carry == 1:
            res.append(1)
        res = res[::-1]
        return res

