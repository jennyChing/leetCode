'''
190. Reverse Bits

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
'''
class Solution:
    def reverseBits(self, n):
        #origin_b = str(bin(n))
        #print(origin_b, type(origin_b))
        #reversed_b = reversed(origin_b)
        #print(reversed_b)
        #return int(reversed_b, 2)
        result = 0
        print(bin(result), bin(n))
        for i in range(32):
            result <<= 1
            result |= n & 1 # get n last digit of n and push it to result to 進位
            print(result)
            n >>= 1
            print("result double: ", result, "n in half: ", n)
            print(bin(result), bin(n))
        return result
if __name__ == '__main__':
    print(Solution().reverseBits(123123123))

