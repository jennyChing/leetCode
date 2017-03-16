'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution(object):
    def generateParenthesis_add_1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
# use general backtracking
        result = []
        left, right = 0, 0 # staring point
        def backtracking(partial, left, right, n):
            if left >= right >= 0: # valid combinations check
                if len(partial) == n * 2: # check if the iteration ends
                    result.append(partial)
                if left < n:
                    backtracking(partial + '(', left + 1, right, n)
                if right < left:
                    backtracking(partial + ')', left, right + 1, n)
        backtracking('', left, right, n)
        return result

    def generateParenthesis_minus_1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(left_remain, right_remain, partial):
            if right_remain == left_remain == 0: # success state: left = right = 0, append partial
                res.append(partial)
                return
            if left_remain and left_remain <= right_remain:
                backtrack(left_remain - 1, right_remain, partial + "(")
            if right_remain and left_remain <= right_remain:
                backtrack(left_remain, right_remain - 1, partial + ")")
        res = []
        backtrack(n, n, "")
        return res


    def generateParenthesis_refer(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(left_remain, right_remain, partial):
            if left_remain:
                backtrack(left_remain - 1, right_remain, partial + '(')
            if right_remain > left_remain:
                backtrack(left_remain, right_remain - 1, partial + ')')
            if not right_remain: # left, right both are zero
                res.append(partial)

        res = []
        backtrack(n, n, "")
        return res

# using generator!!!
      #  def __directed_generate(partial, left_remain, right_remain):
      #  # use partial to record the possible combination
      #      print(partial, right_remain, left_remain)
      #      if right_remain >= left_remain >= 0:
      #      # return when no more right parenthese left
      #          if not right_remain:
      #              print("append result", right_remain)
      #              yield partial
      #          # recursively yield p by using up one of the '('
      #          for p in __directed_generate(partial + '(', left_remain - 1, right_remain):
      #              yield p
      #          # recursively yield p by adding a ')'
      #          for p in __directed_generate(partial + ')', left_remain, right_remain - 1):
      #              yield p
      #  return list(__directed_generate('', n, n))

if __name__ == '__main__':
    res = Solution().generateParenthesis(3)
    print(list(res))
