class Solution(object):
    def twoSum(self, numbers, target):
        '''
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        '''
        dict_pos = {}
        for i in range(len(numbers)):
            dict_pos[target - numbers[i]] = i + 1
        for i in range(len(numbers)):
            if numbers[i] in dict_pos:
                return  [dict_pos[numbers[i]], dict_pos[n]]
if __name__ == '__main__':
    res = Solution().twoSum([0, 0, 3, 4], 0)
    print(res)
