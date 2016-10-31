'''
81. Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

    Write a function to determine if a given target is in the array.
'''
class Solution(object):
    def search(self, nums, target):

# 4 senarios => can use either left or right part to check, using left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            print(mid, nums[mid], target)
        # case 1: nums[mid] = target
            if nums[mid] == target:
                return True

        # case 2: nums[left] < nums[mid], take left half when left < target < mid, else right half
            elif nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        # case 3: nums[left] > nums[mid], take right half when mid < target < right, else left half
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # Case 4: deal with it when left = mid and cannot eliminate either half
            else:
                left += 1

        return False
if __name__ == '__main__':
    nums = [4, 4, 5, 6, 7, 0, 1, 2]
    nums = [1, 1, 1, 2, 4, 1]
    nums = [1]
    res = Solution().search(nums, 4)
    print(res)



