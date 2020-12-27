class Solution:
    def longest_palindrome_by_pd(self, s: str) -> str:
        len_s = len(s)
        dp = [[False] * len_s for _ in range(len_s)]
        ans = ""
        for l in range(len_s):
            for i in range(len_s):
                j = i + l
                if j >= len_s:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

                if dp[i][j] and (l + 1 > len(ans)):
                    ans = s[i : j + 1]

        return ans

    def longest_palindrome_by_expand(self, s: str) -> str:
        len_s = len(s)
        global_ans = ""

        for i in range(len_s - 1):
            ans_around_i = ""
            expand_width = 1
            global_ans_len_is_even = True if s[i] == s[i + 1] else False
            while True:
                left, right = i - expand_width, i + expand_width
                if global_ans_len_is_even:
                    right += 1
                if left < 0 or right >= len_s:
                    break
                if s[left] == s[right]:
                    ans_around_i = s[left : right + 1]

                expand_width += 1

            if len(global_ans) < len(ans_around_i):
                global_ans = ans_around_i

        return global_ans

    def longest_palindrome_manachar(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # expand s
        new_s = ""
        for c in s:
            new_s += "#" + c
        new_s += "#"

        len_new_s = len(new_s)

        radiuses = [0] * len_new_s
        radiuses[1] = 1
        radius = 1
        max_radius = 1
        center = 1
        for i in range(2, len_new_s):
            if i + max_radius >= len(new_s):
                break

            if radius > 1:
                # either use the mirror side radius (radiuses[center *2 - i])
                # or use current radius at center minus the distance from i to center
                current_radius = min(radius - (i - center), radiuses[center * 2 - i])
            else:
                current_radius = 0

            left, right = i - current_radius - 1, i + current_radius + 1
            while True:
                if left >= 0 and right < len(new_s) and new_s[left] == new_s[right]:
                    current_radius += 1
                    left -= 1
                    right += 1
                else:
                    break

            max_radius = max(max_radius, current_radius)
            radiuses[i] = current_radius
            if i + current_radius > center + radius:
                center = i
                radius = current_radius

        begin = radiuses.index(max_radius) // 2 - max_radius // 2
        end = radiuses.index(max_radius) // 2 + max_radius // 2

        return s[begin : end + 1]


print(Solution().longest_palindrome_manachar("baab"))
