class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        len_s = len(s)
        next_start = 0
        replace_num = 0
        repeated_string = s[0]
        max_repeated_len = 1

        i = 1
        while True:
            if repeated_string[-1] == s[i]:
                repeated_string += s[i]
            elif replace_num < k:
                repeated_string += repeated_string[-1]
                if replace_num == 0:
                    next_start = i
                replace_num += 1
            else:
                max_repeated_len = max(max_repeated_len, len(repeated_string))
                repeated_string = s[next_start]
                replace_num = 0
                i = next_start + 1
                if next_start >= len_s - max_repeated_len:
                    break
                else:
                    continue

            max_repeated_len = max(max_repeated_len, len(repeated_string))
            i += 1
            if i >= len_s:
                break

        return max_repeated_len


print(Solution().characterReplacement("AABABBAB", 1))
