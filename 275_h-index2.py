'''
275. H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

(binary search)
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
    # O(logN) solution: do binary search to find the min index such that citations[i] >= len(citations) - i (hight h index coz more paper after index i)
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if citations[mid] >= n - mid:
                print("take left", left, mid, right)
                right = mid - 1 # take the left half
            else:
                left = mid + 1 # take the right half
        print(left, mid, right)
        return  n - left #


    # O(n) solution:
        # criteria1: h of the papers in the citation list, compare the value and index (how many are less then v)
        # criteria2: has at least h citations each, compare value and h
       # h = 0
       # for i, v in enumerate(citations):
       #     print("There are", i, "papers have less citations then current value", v)
       #     print("The remaining", len(citations) - i, "papers should have at least", v, "citations to update the h-index.")
       #     if v >= len(citations) - i  and v > h: # v must compare with the updated h
       #         h = max(h, len(citations) - i)
       #         print(i, v, h)
       #     print()
       #return h

if __name__ == '__main__':
    citations = [6, 5, 3, 0, 1]
    citations = [0, 1, 3, 5, 6]
    res = Solution().hIndex(citations)
    print(res)

