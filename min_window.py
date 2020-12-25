char2_idx = lambda c: ord(c) - ord("A")


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or len(s) < len(t):
            return ""

        t_char_count = [0] * 256
        s_char_count = [0] * 256

        for c in t:
            t_char_count[char2_idx(c)] += 1

        begin, end = -1, -1
        left, right = 0, -1
        len_t_in_s = 0

        while True:
            if len_t_in_s == len(t):
                if left == len(s) - len(t):
                    break
                else:
                    left += 1
                    left_char_idx = char2_idx(s[left - 1])
                    if t_char_count[left_char_idx] > 0:
                        s_char_count[left_char_idx] -= 1
                        len_t_in_s -= 1

            if len_t_in_s < len(t):
                if right == len(s) - 1:
                    break
                else:
                    right += 1
                    right_char_idx = char2_idx(s[right])
                    if s_char_count[right_char_idx] < t_char_count[right_char_idx]:
                        s_char_count[right_char_idx] += 1
                        len_t_in_s += 1

            if len_t_in_s == len(t) and (end - begin > right - left or begin < 0):
                begin, end = left, right

        return s[begin : end + 1]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
