'''
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
'''
import operator
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        recursively traverse the input and split the input into 2 parts
        check the operator is +/-/* and compute the 2 parts result
        """
# Short 1 line version:
        return [a + b if op == '+' else a - b if op == '-' else a * b for i, op in enumerate(input) if op in '-*+' for a in self.diffWaysToCompute(input[:i]) for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]

if __name__ == "__main__":
    res = Solution().diffWaysToCompute('2-1-1')
    res = Solution().diffWaysToCompute('2*3-4*5')
    print(res)




