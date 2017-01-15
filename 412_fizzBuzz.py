'''
412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                res.append("FizzBuzz")
            elif not i % 3:
                res.append("Fizz")
            elif not i % 5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

# refer more neat solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

if __name__ == "__main__":
    res = Solution().fizzBuzz(3)
    print(res)
