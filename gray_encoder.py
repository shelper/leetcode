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

        result = [0, 1]
        for i in range(1, n):
            result.extend([2 ** i + v for v in reversed(result)])

        return result


print([bin(v) for v in Solution().gray_code(10)])
print(Solution().gray_code(10))
