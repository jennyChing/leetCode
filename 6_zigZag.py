'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
And then read line by line: "PAHNAPLSIIGYIR"
'''
class Solution(object):
    def convert(self, s, numRows):
        if not s or numRows == 1:
            return s
        res, step = '', numRows * 2 - 2
        for i in range(numRows):
            for j in range(i, len(s), step):
                res += s[j]
# only for lines except at the first and last row will need to append extra char
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s): # not the first or last row
                    res += s[j + step - 2 * i]
        return res
if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))
