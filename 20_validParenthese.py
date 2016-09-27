'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not
'''
class Solusion(object):
    def isValid(self, s):
        brace_start = {"(":1, "{":1, "[":1}
        paren_stack = []
        for p in s:
            print(paren_stack)
            if p in brace_start:
                paren_stack.append(p)
            elif (p == ")" and paren_stack.pop() != "(") or (p == "]" and paren_stack.pop() != "[") or (p == "}" and paren_stack.pop() != "{"):
                return False
        return True
if __name__ == '__main__':
    s = "[]{}"
    res = Solusion().isValid(s)
    print(res)

