'''
376. Wiggle Subsequence
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
'''
class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        if len(nums) == 2:
            return len(nums) if nums[0] != nums[1] else 1
        up = True if nums[0] >= nums[1] else False
        if up == True:
            nums = [float('-inf')] + nums
        else:
            nums = [float('inf')] + nums
        isUp, temp = True, nums[:1]
        # separate 2 cases: start with isUp = True or False
        print(isUp, temp)
        for n in nums[1:]:
            if n < temp[-1] and isUp == True:
                temp.append(n)
                print(temp)
                isUp = False
            elif n > temp[-1] and isUp == False:
                temp.append(n)
                isUp = True
                print(temp)
            else:
                temp[-1] = n
        return len(temp) - 1
if __name__ == '__main__':
    nums = [1,17,5,10,13,15,10,5,16,8]
    nums = [1,7,4,9,2,5]
    nums = [3,3,3,2,5]
    res = Solution().wiggleMaxLength(nums)
    print(res)




