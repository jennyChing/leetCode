'''
116. Populating Next Right Pointers in Each Node

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
         1
       /  \
      2    3
     / \  / \
    4  5  6  7

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root != None:
            level_start = [root]
            curr = root
            while curr.left:
                level_start.append(curr)
                print(curr.val)
                while curr:
                    # first connect left and right child
                    curr.left.next = curr.right
                    # same level
                    curr.right.next = curr.next.left if curr.next else None
                    curr = curr.next
                # go down 1 level
                curr = level_start.pop().left
if __name__ == "__main__":
    t1 = TreeLinkNode(1)
    t1.left = TreeLinkNode(2)
    t1.right = TreeLinkNode(3)
    t1.left.left = TreeLinkNode(4)
    t1.left.right = TreeLinkNode(5)
    t1.right.left = TreeLinkNode(6)
    t1.right.right = TreeLinkNode(7)
    Solution().connect(t1)
    print(t1.right.left.next.val)


