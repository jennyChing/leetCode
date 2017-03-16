'''
117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

import collections
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # idea: use bfs traversal to point right to next node on the right
        if not root:
            return
        currLevel = collections.deque([root])
        while currLevel:
            nextLevel = collections.deque([])
            while currLevel:
                node = currLevel.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                node.next = currLevel[0] if currLevel else None
            currLevel = nextLevel

    def connect_linkedList(self, root):
        node, level, cur = root, None, None
        while node:
            print(node.val, level, cur)
            if node.left:
                if not level: # update level to most right node in this level
                    level = cur = node.left
                else:
                    cur.next = node.left
                    cur = cur.next
            if node.right:
                if not level: # update level to most right node in this level
                    level = cur = node.right
                else:
                    cur.next = node.right
                    cur = cur.next
            node = node.next
            if not node and level: # reset and move to next level
                node, level, cur = level, None, None

if __name__ == "__main__":
    t1 = TreeLinkNode(1)
    t1.left = TreeLinkNode(2)
    t1.right = TreeLinkNode(3)
    t1.left.left = TreeLinkNode(4)
    t1.left.right = TreeLinkNode(5)
    t1.right.left = TreeLinkNode(6)
    t1.right.right = TreeLinkNode(7)
    Solution().connect_linkedList(t1)
    print(t1.right.left.next.val)

