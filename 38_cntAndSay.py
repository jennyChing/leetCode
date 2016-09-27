class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"
        for _ in range(n):
            cnt, temp, last = 0, "", seq[0]
            for s in seq:
                if s == last:
                    cnt += 1
                else:
                    temp = temp + str(cnt) + last
                    last = s
                    cnt = 1
            temp = temp + str(cnt) + s
            print("going through", seq, "what we have now :", temp)
            seq = temp
        return seq
if __name__ == '__main__':
    print(Solution().countAndSay(9))
