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
        split_input = []

# Step1: parsing, split the input by operators
        opdict = {'*':operator.mul, '-': operator.sub, '+':operator.add}
        input+= '-'
        print(input)
        i = 0
        for j in range(len(input)):
            if input[j] in opdict:
                print(input[j], input, i, j)
                split_input.append(int(input[i:j]))
                split_input.append(input[j])
                print(split_input)
                i = j + 1
        split_input = split_input[:-1]
        print(split_input, "Step2 :")

# Step 2: Recursive function:
        def __directed_compute(split_input):
            if len(split_input) == 1:
                return [split_input[0]]
            res = []

            for i, v in enumerate(split_input):
                if isinstance(v, str) and v in "*-+":
                    left, right = __directed_compute(split_input[:i]), __directed_compute(split_input[i + 1:])
                    print(left, right)
                    for l in left:
                        for r in right:
                            if v == '*':
                                res.append(l * r)
                            elif v == '-':
                                res.append(l - r)
                            elif v == '+':
                                res.append(l + r)
            return res
        return __directed_compute(split_input)

if __name__ == "__main__":
    res = Solution().diffWaysToCompute('2-1-1')
    res = Solution().diffWaysToCompute('2*3-4*5')
    print(res)




