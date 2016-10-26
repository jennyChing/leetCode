class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        def __is_intersect(a1, a2, b1, b2):
            return (a2 >= b1 and a1 <= b2) or (b2 >= a1 and b1 <= a2)

        area = (C - A) * (D - B) + (G - E) * (H - F)
        if __is_intersect(A, C, E, G) and __is_intersect(B, D, F, H):
            area -= (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return area


if __name__ == "__main__":
    res = Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    print(res)
