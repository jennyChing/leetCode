import collections

class Solution(object):
    def getHint(self, secret, guess):
        a, b, = 0, 0
        s_lookup, g_lookup = collections.defaultdict(int), collections.defaultdict(int)
        print(s_lookup, g_lookup)
        for s, g in zip(secret, guess):
            if s == g:
                 a += 1
            else:
                if s_lookup[g]:
                    s_lookup[g] -= 1
                    b += 1
                else:
                    g_lookup[g] += 1
                if g_lookup[s] :
                    g_lookup[s] -= 1
                    b += 1
                else:
                    s_lookup[s] += 1
        return '%dA%dB' % (a, b)
if __name__ == '__main__':
    res = Solution().getHint('1807', '7810')
    print(res)



