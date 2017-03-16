'''
307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''
class TreeNode(object):
    def __init__(self, start, end):
        self.right = None
        self.left = None
        self.start = start
        self.end = end
        self.val = 0

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        start, end = 0, len(nums)
        self.nums = nums
        self.root = self.build_tree(TreeNode(start, end)) if start != end else None

    def build_tree(self, curr):
        if curr.start + 1 == curr.end:
            curr.val = self.nums[curr.start]
            return curr
        mid = (curr.start + curr.end) // 2
        curr.left = self.build_tree(TreeNode(curr.start, mid))
        curr.right = self.build_tree(TreeNode(mid, curr.end))
        curr.val = curr.left.val + curr.right.val
        return curr

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def _update(root):
            if i == root.start == root.end - 1: # i reach target index
                root.val = val
                return
            if i < root.start or i >= root.end: # i is out of range
                return
            _update(root.right) # traverse right subtree
            _update(root.left) # traverse left subtree
            root.val = root.right.val + root.left.val
        _update(self.root)


    def sumRange(self, i, j): # query sum of nums[i:j]
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def _sumRange(root):
            if i <= root.start and root.end <= j: # complete overlap
                return root.val
            if j <= root.start or i >= root.end: # no overlap
                return 0
            return _sumRange(root.left) + _sumRange(root.right) # partial overlap

        j = j + 1
        return _sumRange(self.root)



# Your NumArray object will be instantiated and called as such:
if __name__ == "__main__":
    nums = [3, 2, -1, 6, 5]
    numArray = NumArray(nums)
    numArray.update(1, 10)
    print(numArray.sumRange(1, 2))

