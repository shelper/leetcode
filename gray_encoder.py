class Solution(object):
    def gray_code(self, n: int):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return None

        if n == 1:
            return [0, 1]

        return [2 ** (n - 1) + v for v in self.gray_code(n - 1)] + list(
            reversed(self.gray_code(n - 1))
        )
        # list.reverse() only change local list but return only None


print([bin(v) for v in Solution().gray_code(10)])
