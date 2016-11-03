'''
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_to_letter = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        # recursive version
        def __directed_search(i, partial):
            if len(partial) == len(digits):
                res.append(partial)
                return
            for c in dig_to_letter[digits[i]]:
                partial += c
                print(i, c, partial, digits[i])
                __directed_search(i + 1, partial)
                partial = partial[:-1]

        __directed_search(0, "")

        # short version
        #for d in digits:
            # res = [i + ch for i in res for ch in dig_to_letter[d]]
        return res

if __name__ == '__main__':
    nums = "23"
    res = Solution().letterCombinations(nums)
    print(res)
