import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, head):
        '''
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        '''
        self.nums = nums
        self.reset = lambda: nums
        print(self.reset)

    def getRandom(self):
        '''
        :rtype: List[int]
        randomly generate a number corresponding to the index of the List and remove the List[number] then continue to randomly generate the next number
        '''
        res = ListNode(0)
        temp = self.head[:] # use [:] to copy instead of assign
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




