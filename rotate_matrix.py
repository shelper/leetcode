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
            for j in range(i, n - i - 1):
                mat[j][n - i - 1] = v
                v += 1
            for j in range(n - i - 1, 0, -1):
                mat[n - i - 1][j] = v
                v += 1
            for j in range(n - i - 1, i, -1):
                mat[j][i] = v
                v += 1

        if n % 2:
            mat[n // 2][n // 2] = n ** 2 - 1

        for m in mat:
            print(m)

    def rotate_mat_recursive(self, n):
        mat = [[0] * n for i in range(n)]

        def fill(mat_size):
            corner_idx = (n - mat_size) // 2
            start_value = n ** 2 - mat_size ** 2
            if mat_size == 1:
                mat[corner_idx][corner_idx] = start_value
                return
            else:
                for i in range(0, mat_size - 1):
                    mat[corner_idx][corner_idx + i] = start_value + i
                    mat[corner_idx + i][corner_idx + mat_size - 1] = (
                        start_value + i + mat_size - 1
                    )
                    mat[corner_idx + mat_size - 1][corner_idx + mat_size - 1 - i] = (
                        start_value + i + (mat_size - 1) * 2
                    )
                    mat[corner_idx + mat_size - 1 - i][corner_idx] = (
                        start_value + i + (mat_size - 1) * 3
                    )

            if mat_size == 2:
                return
            return fill(mat_size - 2)

        fill(n)
        for m in mat:
            print(m)


Solution().rotate_mat(5)
Solution().rotate_mat_recursive(5)
