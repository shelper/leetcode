class Solution:
    def largest_rec(self, l):
        res = 0
        stack = []
        # stack = [[-1, 0]]
        l.append(0)

        for i, n in enumerate(l):
            if not stack:
                stack.append([i, n])
                continue

            if n > stack[-1][1]:
                stack.append([i, n])
            else:
                while stack and n < stack[-1][-1]:
                    stack_top = stack.pop(-1)
                    left_bound = stack[-1][0] if stack else -1
                    right_bound = i - 1
                    res = max(res, (right_bound - left_bound) * stack_top[1])

                if not stack or n > stack[-1][-1]:
                    stack.append([i, n])

        return res


print(Solution().largest_rec([2, 1, 5, 6, 2, 3]))
