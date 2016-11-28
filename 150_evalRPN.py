'''
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums, opers = [], []
        for t in tokens:
            if t in '+-*/':
                r = nums.pop()
                l = nums.pop()
                if t == '+':
                    nums.append(l + r)
                elif t == '-':
                    nums.append(l - r)
                elif t == '*':
                    nums.append(l * r)
                else:
		    # here take care of the case like "1/-22",
		    # in Python 2.x, it returns -1, while in
		    # Leetcode it should return 0
                    if l * r < 0 and l % r != 0:
                        nums.append(l // r + 1)
                    else:
                        nums.append(l/r)
            else:
                nums.append(int(t))
        return nums.pop()

if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10","6","9","3","+","-11","*","/","*"]
    res = Solution().evalRPN(tokens)
    print(res)
