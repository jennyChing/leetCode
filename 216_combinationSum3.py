'''
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        Backtracking
        """
        if n > 9 * k:
            return []
        res = []
        # Step1: starting point: start from 1
        def __directed_combination(k, n, partial, start, res):
            # Step3: Append the valid combination to the result array
            if k == 0 and n == 0:
                res.append(partial)
                print(res)
                return res
            for i in range(start, 10):
                # Step2:  validate and recursive the rest part
                if i <= n:
                    __directed_combination(k - 1, n - i, partial + [i], i + 1, res)
            return res

        return  __directed_combination(k, n, [], 1, [])
if __name__ == "__main__":
    res = Solution().combinationSum3(3, 9)
    print(res)


