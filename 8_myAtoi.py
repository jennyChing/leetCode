class Solution(object):
    def myAtoi(self, str):
        if not str:
            return 0
        # get rid of white spaces
        str = str.strip()
        # start parsing
        sign = -1 if str[0] = '-' else 1
        if str[0] in ('+', '-'):
            str = str[1:]
        i, res = 0, 0
        while i < len(str) and str[i].isdigit():
            res = res * 10 + ord(str[i] - ord('0'))
            i += 1
        return max(min(sign * res, 2**31 - 1), -2**31)

