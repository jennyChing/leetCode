import random
class Solution(object):
    def __init__(self, nums):
        '''
        type nums: List[int]
        '''
        self.nums = nums
        self.reset = lambda: nums
        print(self.reset)

    def reset(self):
        '''
        :rtype: List[int]
        '''
        return self.reset

    def shuffle(self):
        '''
        :rtype: List[int]
        randomly generate a number corresponding to the index of the List and remove the List[number] then continue to randomly generate the next number
        '''
        res = []
        temp = self.nums[:] # use [:] to copy instead of assign
        while temp:
            ran = random.randrange(len(temp))
            res.append(temp[ran])
            temp.remove(temp[ran])
        return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution(nums)
    print(res.reset())
    print(res.shuffle())
    print(res.reset())




