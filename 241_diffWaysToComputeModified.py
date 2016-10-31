'''
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
'''
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        recursively traverse the input and split the input into 2 parts
        check the operator is +/-/* and compute the 2 parts result
        """
        res = []
        for i, v in enumerate(input):
            if v in '-*+':
                left, right = self.diffWaysToCompute(input[:i]), self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        res.append(l + r if v == '+' else l - r if v == '-' else l * r)
        # base case: no result is appended so the substring is an int
        #if not res:
        #    res.append(int(input))
        #return res
        return res or [int(input)] # empty result array

if __name__ == "__main__":
    res = Solution().diffWaysToCompute('2-1-1')
    res = Solution().diffWaysToCompute('2*3-4*5')
    print(res)




