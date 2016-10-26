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
        res = []
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
        def __directed_compute(split_input, partial, res):
            print("sub input :", split_input)
            if len(split_input) == 1:
                partial += split_input[0]
                return partial
            if len(split_input) == 3:
                a, op, b = split_input[0], split_input[1], split_input[2]
                print(a, op, b)
                partial += a * b if op == '*' else a + b if op == '+' else a - b
                return partial

            for i in range(len(split_input)):
                if split_input[i] == '+':
                    print("before", partial)
                    partial = __directed_compute(split_input[:i], partial, res) + __directed_compute(split_input[i + 1:], partial, res)
                    print("result", partial)
                elif split_input[i] == '*':
                    print("before", partial, split_input[:i], split_input[i + 1])
                    partial = __directed_compute(split_input[:i], partial, res) * __directed_compute(split_input[i + 1:], partial, res)
                    print("result", partial)
                elif split_input[i] == '-':
                    print(partial)
                    partial = __directed_compute(split_input[:i], partial, res) - __directed_compute(split_input[i + 1:], partial, res)
                    print("result", partial)
                res.append(partial)
            print(res)
        __directed_compute(split_input, 0, [])
        return res
if __name__ == "__main__":
    res = Solution().diffWaysToCompute('2-1-1')
    res = Solution().diffWaysToCompute('2*3-4*5')
    print(res)




