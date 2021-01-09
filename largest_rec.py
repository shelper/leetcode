class Solution:
    def largest_rec(self, l):
        res = 0
        stack = []
        l.append(-1)  # this will help to deal with the last number

        # start calculating area
        for i, n in enumerate(l):
            if not stack or n > stack[-1][1]:
                stack.append([i, n])
            else:
                while stack[-1][1] > n:
                    stack_top = stack.pop(-1)
                    left_bound = stack[-1][0] if stack else -1
                    right_bound = i - 1
                    res = max(res, (right_bound - left_bound) * stack_top[1])

                    if not stack:  # quick this loop if stack is emptied after pop
                        break

                # reset the stack after been popped above
                if not stack or n > stack[-1][1]:
                    stack.append([i, n])
                elif n == stack[-1][1]:
                    stack[-1][0] = i

        return res


print(Solution().largest_rec([0, 0, 0, 0, 0, 0, 1, 1, 5, 5, 1, 6, 2, 3, 2, 2, 2, 0]))
