class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_elm, start = max(nums), 0
        isAllSame = True
        l_arr, r_arr = [], []
        if k == 1:
            return nums[i]
        for i in range(len(nums)):
            if nums[i] == max_elm:
                r_arr.append(nums[i])
            elif nums[i] != max_elm:
                start = i
                partition = nums[i]
                isAllSame = False
                break
        print(start)
        if isAllSame == False:
            for n in nums[start + 1:]:
                if n > partition and len(r_arr) + 1 >= k:
                    l_arr.append(min(n, partition))
                    partition = max(n, partition)
                    print("right overboubd :", l_arr, partition, r_arr)
                elif n < partition and len(l_arr) + 1 > len(nums) - k:
                    r_arr.append(max(n, partition))
                    partition = min(n, partition)
                    print("left overbound :", l_arr, partition, r_arr)
                else:
                    if n > partition:
                        r_arr.append(n)
                    else:
                        l_arr.append(n)
                    print("not overbound :", l_arr, partition, r_arr)
                print(n, l_arr)
        print(l_arr, partition, r_arr)
        return nums[0] if isAllSame == True else partition

if __name__ == '__main__':
    nums = [3,2,11,5,6,4]
    nums = [2, 1]
    nums = [3,1,2,4]
    nums = [-1,2,0]
    nums = [7,6,5,4,3,2,1]
    k = 5
    res = Solution().findKthLargest(nums, k)
    print(res)
