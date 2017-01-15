'''
475. Heaters

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
'''
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        min_r = 0
        heaters.sort()
        for h in houses:
            l, r = 0, len(heaters) # left included, right not included
            while l < r: # binary seach find closest heater to update min_r
                mid = (l + r) // 2
                print(mid, heaters[mid])
                if heaters[mid] == h:
                    break # radius = 0
                elif heaters[mid] < h:
                    l = mid + 1 # take right half
                else:
                    r = mid # take left half
            #print(heaters[mid], mid, h)
# Calculate the distances between this house and left heater and right heater, get a MIN value of those two values. Corner cases are there is no left or right heater.
            leftHeaterDistance = h - heaters[l - 1] if l > 0 else sys.maxint
            rightHeaterDistance = heaters[l] - h if l < len(heaters) else sys.maxint
            min_r = max(min_r, min(leftHeaterDistance, rightHeaterDistance))
        return min_r

if __name__ == "__main__":
    houses, heaters = [1], [1,2,3,4]
    houses, heaters = [1,2,3,4], [1,4]
    res = Solution().findRadius(houses, heaters)
    print(res)
