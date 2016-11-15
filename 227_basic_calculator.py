'''
227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # use stack to store last added nums to do the calculation
        stack, num, sign = [], 0, "+" # sign keep record of the last operator to do calculation
        for i, v in enumerate(s):
            if v.isdigit():
                num = num * 10 + ord(v) - ord("0")
            if v in '+-/*' or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = v # record this sign to do calculation for next num
                num = 0
        return sum(stack)


if __name__ == "__main__":
    s = "3+2*2 + 1*3*44"
    res = Solution().calculate(s)
    print(res)
