'''
46. Permutations

Given a collection of distinct numbers, return all possible permutations.
'''
class Solution(object):
    def permute(self, nums):
        def permutations(nums):
            if not nums:
                yield []
            for n in nums:
                print(n)
                for p in permutations([i for i in nums if i != n]):
                    yield [n] + p
                    #print(n, p, [n] + p)

        return [p for p in permutations(nums)]

# Backtracking burceforce solution! compare with others~~~
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # idea: dfs backtricking solution
        def dfs(partial):
            if len(partial) == len(nums):
                res.append(partial) # main checking condition
                return
            # if not valid partial
            for n in nums: # no need level to record start coz iterate all!
                print(partial)
                if n in partial:
                    continue # already in the partial list
                dfs(partial + [n]) # generate new dfs

        res = []
        dfs([])
        return res

if __name__ == '__main__':
    res = Solution().permute([1,2,3])
    print(res)
