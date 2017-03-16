'''
393. UTF-8 Validation

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
'''
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i, chars = 0, 0
        while i < len(data):
         #if bin(data[i])[2:].zfill(8)[0] == "0": # character is 1 byte long
            if data[i] < 128:
                i += 1
                continue

            chars = 0 # possible length: 2 ~ 4 (1 ~ 3 characters)
            for b in bin(data[i])[2:].zfill(8): # character is 2~4 byte long
                if b == "1":
                    chars += 1
                else:
                    break
            if chars == 1 or chars > 4 or i + chars > len(data): return False
            for j in range(1, chars): # check next 2~4 bytes
                if bin(data[i + j])[2:].zfill(8)[:2] != "10":
                    return False
            i += chars
        return True

# refer
def check(nums, start, size):
    for i in range(start + 1, start + size + 1):
        if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
    return True

class Solution(object):
    def validUtf8(self, nums, start=0):
        while start < len(nums):
            first = nums[start]
            print(first >> 3, start)
            if   (first >> 3) == 0b11110 and check(nums, start, 3): start += 4
            elif (first >> 4) == 0b1110  and check(nums, start, 2): start += 3
            elif (first >> 5) == 0b110   and check(nums, start, 1): start += 2
            elif (first >> 7) == 0:                                 start += 1
            else:                                                   return False
        return True


if __name__ == "__main__":
    data = [235, 140, 4]
    data = [240,162,138,147,17]
    data = [39,89,227,83,132,95,10,0]
    data = [197, 130, 1]
    data = [250,145,145,145,145]
    res = Solution().validUtf8(data)
    print(res)
