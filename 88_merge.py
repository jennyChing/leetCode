'''
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        divide and conquer 2 sorted array
        """
# not a good approach to insert... using correct placement from the back is better
        #i, j = 0, 0
        #if m == 0:
        #    nums1 = nums2
        #elif n != 0:
        #    while i < m and j < n:
        #        if nums1[i] < nums2[j]:
        #            nums1.insert(i - 1, nums2[j])
        #            i += 1
        #            j += 1
        #        else:
        #            i += 1
        #return nums1
        i, j = m - 1, n - 1
        write_from_back = m + n - 1
        while i >= 0 and j >= 0:
            print(write_from_back, i, j, nums1[i], nums2[j], nums1)
            if nums1[i] > nums2[j]:
                nums1[write_from_back] = nums1[i]
                i -= 1
            else:
                nums1[write_from_back] = nums2[j]
                j -= 1
            write_from_back -= 1
        while j >= 0: # num2 is not done yet
            print(write_from_back, i, j, nums1[i], nums2[j], nums1)
            nums1[write_from_back] = nums2[j]
            j -= 1
            write_from_back -= 1
        return nums1

if __name__ == '__main__':
    nums1, m, nums2, n = [0, 3, 4, 6, 0, 0, 0, 0], 4, [1, 2, 7, 8], 4
    print(Solution().merge(nums1, m, nums2, n))
