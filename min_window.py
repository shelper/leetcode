class Solution(object):
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or len(s) < len(t):
            return ""

        t_char_count = {}
        substring_char_count = {}

        for c in t:
            t_char_count[c] = t_char_count.get(c, 0) + 1

        begin, end = -1, -1
        left, right = 0, 0
        len_t_in_s = 0

        while True:
            if len_t_in_s == len(t):
                if left == len(s) - len(t):
                    break
                else:
                    left += 1
                    removed_char = s[left - 1]
                    if t_char_count.get(removed_char, 0) > 0:
                        substring_char_count[removed_char] -= 1
                        if (
                            substring_char_count[removed_char]
                            < t_char_count[removed_char]
                        ):
                            len_t_in_s -= 1

            if len_t_in_s < len(t):
                if right == len(s):
                    break
                else:
                    right += 1
                    added_char = s[right - 1]  # the count - 1 is the index
                    if t_char_count.get(added_char, 0) > 0:
                        substring_char_count[added_char] = (
                            substring_char_count.get(added_char, 0) + 1
                        )
                        if substring_char_count.get(added_char) <= t_char_count.get(
                            added_char
                        ):
                            len_t_in_s += 1

            if len_t_in_s == len(t) and (end - begin > right - left or begin < 0):
                begin, end = left, right

        return s[begin:end]


print(Solution().min_window("ADOBECODEBANC", "ABC"))
