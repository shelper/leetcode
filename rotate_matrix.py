class Solution:
    def rotate_mat(self, n):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mat = [[0] * n for i in range(n)]
        v = 0
        for i in range(0, n // 2):
            for j in range(i, n - i - 1):
                mat[i][j] = v
                v += 1
            for k in range(i, n - i - 1):
                mat[k][n - i - 1] = v
                v += 1
            for m in range(n - i - 1, 1, -1):
                mat[n - i - 1][m] = v
                v += 1
            for l in range(n - i - 1, i, -1):
                mat[l][i] = v
                v += 1

        if n % 2:
            mat[n // 2][n // 2] = n ** 2 - 1

        for m in mat:
            print(m)


Solution().rotate_mat(5)
Solution().rotate_mat(4)
