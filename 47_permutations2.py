'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    print(i, l, new_ans)
                    if i < len(l) and l[i] == n:
                        print("skip")
                        break
            ans = new_ans
        return ans

# idea: dfs backtricking solution
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
# idea: memo keep the visited index; cache keep the used value to avoid repeat
        def dfs(partial, memo):
            print(partial, memo)
            if len(partial) == len(nums):
                res.append(partial) # main checking condition
                return
            # if not valid partial
            cache = set()
            for i in range(len(nums)):
                if i in memo or nums[i] in cache:
                    continue
                memo.add(i)
                cache.add(nums[i])
                dfs(partial + [nums[i]], memo) # generate new dfs
                memo.remove(i)

        res = []
        dfs([], set())
        return res

# [Compare with #90]
# [Idea:] if you skip this one, if next one is duplicate one, you cannot choose it. So sort it and while recursing check if the current one is same as the last one, then skip it
        #nums = sorted(nums) # sort it to better check the duplication
        #res = []
        #def __directed_dfs(res, level, path):
        #    print(path)
        #    # complete a path whenever recursive is called and check length
        #    if len(path) == len(nums):
        #        res.append(path)

        #    # start for loop from new level
        #    for i in range(level, len(nums)):
        #        print(level, i, nums[level])
        #    # [Special case to handle:] if the next one is a duplicated value and previous wan't selected: cannot select it! (must skip case)
        #        if i > level and nums[i] == nums[i - 1]: # i > level: skipped
        #            continue # need to skip this duplicate value as well
        #        __directed_dfs(res, i + 1, path + [nums[i]]) # new level is (i + 1) not (level + 1)!

        #__directed_dfs(res, 0, [])
        #return res

if __name__ == "__main__":
    nums = [1, 1, 2]
    res = Solution().permuteUnique(nums)
    print(res)
