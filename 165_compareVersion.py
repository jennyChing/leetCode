class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        def makeSameLen(v1, v2):
            for _ in range(len(v1) - len(v2)):
                v2.append(0)
            return v2
        if len(v1) > len(v2):
            v2 = makeSameLen(v1, v2)
        else:
            v1 = makeSameLen(v2, v1)
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
if __name__ == '__main__':
    res = Solution().compareVersion("1.1", "1")
    print(res)

