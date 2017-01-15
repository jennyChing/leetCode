'''
401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''
import itertools
memo = {}
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        memo
        if num in memo:
            return memo[num]
        res = []
        for n in range(num + 1):
            #print("hour:", n, "minute:", num - n)
            hour = "1" * n + "0" * (4 - n)
            minu = "0" * (6 - num + n) + "1" * (num - n)
            h_list, m_list = set(), set()
            for p in itertools.permutations(hour):
                h_list.add(p)
            for p in itertools.permutations(minu):
                m_list.add(p)
            for h in h_list:
                hours = 0
                for b in h:
                    hours <<= 1
                    hours += int(b)
                if hours > 11: continue
                for m in m_list:
                    mins = 0
                    for b in m:
                        mins <<= 1
                        mins += int(b)
                    if mins > 59: continue
                    res.append(str(hours) + ":" + "0" * (mins < 10) + str( mins))
            #print(res)
        memo[num] = res
        return res

    def readBinaryWatch_dfs(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def dfs(num, hours, mins, idx):
            if hours > 11 or mins > 59: return # not valid
            if not num: # base case when reach end of num
                res.append(str(hours) + ":" + "0" * (mins < 10) + str( mins))
                return
            for i in range(idx, 10): # hours index: 0~3; minus index: 4~9
                if i < 4:
                    dfs(num - 1, hours | (1 << i), mins, i + 1) # recurse
                    print("num:", num, "idx:", idx, "hour:", hours, "min:", mins)
                    print(hours | 1 << i)
                else:
                    k = i - 4
                    dfs(num - 1, hours, mins | (1 << k), i + 1) # recurse
        res = []
        dfs(num, 0, 0, 0)
        return res

    def readBinaryWatch_faster(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]
# turn h and m into binary representation and count the 1s if = num then add to result list

if __name__ == "__main__":
    num = 3
    res = Solution().readBinaryWatch_dfs(num)
    print(res)

