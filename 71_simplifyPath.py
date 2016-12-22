'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        stack = []
        for p in paths:
            if p == '..':
                if len(stack) != 0:
                    stack.pop()
            elif p in ' .':
                continue
            else:
                stack.append(p)
        return "/" + "/".join(stack)

if __name__ == '__main__':
    path = "/a/./b/../../c/"
    s = Solution().simplifyPath(path)
    print(s)

