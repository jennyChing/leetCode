'''
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
import collections
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        ex: 7,0/7,1 -> 7,0/6,1/7,1 (insert 6,1 before index 1) -> 5,0/7,0/5,2/6,1/7,1 (insert 5,2 before index 2) -> 5,0/7,0/5,2/6,1/4,4/7,1 (insert 4,4 before index 4)
        """
        # Step1: sort the list (key = height)
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: x[0], reverse=True)
        res = []
        # Step2: for loop the sorted list and insert people into the new list (insert at the position of k)
        for p in people:
            res.insert(p[1], p)
        return res


if __name__ == "__main__":
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    res = Solution().reconstructQueue(people)
    print(res)
