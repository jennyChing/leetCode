'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
'''
from collections import deque
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        Step1: use for loop to find bull and delete it
        Step2: use hash table to match out cows
        """
        del_bulls = deque()
        bull, cow = 0, 0
        arr_s, arr_g = [], []
        for s in secret:
            arr_s.append(s)
        for g in guess:
            arr_g.append(g)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                del_bulls.appendleft(i)

        for d in del_bulls:
            print(d, arr_s, arr_g)
            arr_s.pop(d)
            arr_g.pop(d)
        dict_secret = {}
        for i in range(len(arr_s)):
            if arr_s[i] not in dict_secret:
                dict_secret[arr_s[i]] = 1
            else:
                dict_secret[arr_s[i]] += 1
        for i in range(len(arr_g)):
            if arr_g[i] in dict_secret and dict_secret[arr_g[i]] >= 1:
                cow += 1
                dict_secret[arr_g[i]] -= 1
        return '%dA%dB' % (bull, cow)

import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = cow = 0
        i = 0
        # first find bulls and remove them from secret and guess
        while i < len(guess):
            if guess[i] == secret[i]:
                bull += 1
                guess = guess[:i] + guess[i + 1:] if i + 1 < len(guess) else guess[:i]
                secret = secret[:i] + secret[i + 1:] if i + 1 < len(secret) else secret[:i]
            else:
                i += 1
        # then find cows in the left secret and guess
        cnt_g, cnt_s = collections.Counter(guess), collections.Counter(secret)
        for k, v in cnt_g.items():
            if k in cnt_s:
                cow += min(v, cnt_s[k])
        return str(bull) + 'A' + str(cow) + 'B'

if __name__ == '__main__':
    res = Solution().getHint("1807", "7810")
    assert res == "1A3B"
    print(res)
    res = Solution().getHint("11", "11")
    assert res == "2A0B"
    print(res)

