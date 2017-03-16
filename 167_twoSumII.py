class Solution(object):
    def twoSum(self, numbers, target):
        '''
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        '''
        dict_pos = {}
        for i, v in enumerate(numbers):
            dict_pos[target - v] = i + 1
        for i, v in enumerate(numbers):
            if v in dict_pos:
                return [i + 1, dict_pos[v]]

    def twoSum_binarySearch(self, numbers, target):
        '''
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        '''
        for i, v in enumerate(numbers):
            l, r = i + 1, len(numbers) - 1
            tmp = target - v
            while l <= r:
                mid = (l + r) // 2
            if numbers[mid] == tmp:
                return [i + 1, mid + 1]
            elif numbers[mid] < tmp:
                l = mid + 1
            else:
                r = mid - 1


if __name__ == '__main__':
    res = Solution().twoSum_binarySearch([0, 0, 3, 4], 0)
    print(res)
