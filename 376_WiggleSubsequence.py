'''
376. Wiggle Subsequence
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
'''
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	# boundary condition
        if len(nums) < 2:
            return len(nums)
        if len(nums) == 2:
            return len(nums) if nums[0] != nums[1] else 1

        unique = [nums[0]]
        for i, v in enumerate(nums):
            if i > 0 and v != nums[i - 1]:
                unique.append(nums[i])

        # boundary condition
        if len(unique) < 2:
            return len(unique)
        if len(unique) == 2:
            return len(unique) if unique[0] != unique[1] else 1

        initUp = False if unique[0] >= unique[1] else True
        wiggle = []
        if initUp == False:
            unique = [float('-inf')] + unique
            isUp = True
        else:
            unique = [float('inf')] + unique
            isUp = False
        for i, v in enumerate(unique[1:]):
            if v > unique[i] and isUp == True:
                #print("peak", v)
                wiggle.append(v)
                isUp = False
            elif v < unique[i] and isUp == False:
                #print("valley", v)
                wiggle.append(v)
                isUp = True
        return len(wiggle)

class oldSolution(object):
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

# second time
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: check the first 2 elements to see if n[0] < n[1] (insert inf to idx 0) or n[0] > n[1] (insert -inf to idx 0)
        nums = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]] # santize duplicated value
        if len(nums) < 3:
            print(nums)
            return len(nums)
        isUp = True if nums[0] > nums[1] else False
        nums = [-sys.maxint] + nums if isUp else [sys.maxint] + nums
        res = 0
        for i, n in enumerate(nums):
            if (isUp and nums[i] > nums[i - 1]) or (not isUp and nums[i] < nums[i - 1]):
                res += 1
                isUp = True if not isUp else False
        return res

if __name__ == '__main__':
    nums = [1,17,5,10,13,15,10,5,16,8]
    nums = [1,7,4,9,2,5]
    res = Solution().wiggleMaxLength(nums)
    print(res)





