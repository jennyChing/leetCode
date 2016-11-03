'''
372. Super Pow

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
'''
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        cycle = self.find_cycle(a)
        print(cycle)
        cycle_length = len(cycle)

        r = 0
        for i in b:
            r = (r * 10 + i) % cycle_length
        return cycle[r - 1]

    def find_cycle(self, a):
        r = a % 1337
        cycle = []
        while r not in cycle:
            print(r in cycle)
            cycle.append(r)
            r = r * a % 1337
        return cycle


if __name__ == '__main__':
    res = Solution().superPow(2, [1, 0, 3])
    print(res)

