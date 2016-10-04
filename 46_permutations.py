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
                for p in permutations([i for i in nums if i != n]):
                    yield [n] + p
                    print(n, p, [n] + p)

        return [p for p in permutations(nums)]

if __name__ == '__main__':
    res = Solution().permute([1,2,3])
    print(res)
