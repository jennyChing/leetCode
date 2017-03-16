'''
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
    Given "25525511135",

    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
# find all valid IP: 4 columns each contain a value 1~255
        def __directed_dfs(k, path, s):
            if len(s) > k * 3: # max is 3 位數
                return
            if k == 0:
                res.append(path)
            else:
                for i in range(min(3, len(s) - k + 1)):
                    if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                        continue # invalid IP
                    __directed_dfs(k - 1, path + [s[:i + 1]], s[i + 1:]) # s[:i + 1] is used
        res = []
        __directed_dfs(4, [], s)
        print(res)
        return ['.'.join(r) for r in res]

if __name__ == "__main__":
    res = Solution().restoreIpAddresses("25525511135")
    print(res)
