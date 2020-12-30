class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        len_s = len(s)
        if len_s <= 1:
            return len_s

        next_start = 0
        replace_num = 0
        repeated_char = s[0]
        repeated_len = 1
        max_repeated_len = 1

        i = 1
        while True:
            if repeated_char == s[i]:
                repeated_len += 1
                i += 1
                if i >= len_s:
                    max_repeated_len = max(
                        max_repeated_len,
                        repeated_len + min(k - replace_num, len_s - repeated_len),
                    )
                    break
            elif k == 0:
                max_repeated_len = max(max_repeated_len, repeated_len)
                next_start = i
                repeated_char = s[next_start]
                repeated_len = 1
                if next_start >= len_s - max_repeated_len:
                    break
                i = next_start + 1
            else:
                if replace_num < k:
                    repeated_len += 1
                    replace_num += 1
                    # mark the first change as new start for next search
                    if replace_num == 1:
                        next_start = i
                    i += 1
                    if i >= len_s:
                        max_repeated_len = max(
                            max_repeated_len,
                            repeated_len + min(k - replace_num, len_s - repeated_len),
                        )
                        break
                else:
                    max_repeated_len = max(max_repeated_len, repeated_len)
                    repeated_char = s[next_start]
                    repeated_len = 1
                    replace_num = 0
                    i = next_start + 1
                    if next_start > len_s - max_repeated_len:
                        break

        return max_repeated_len

    def characterReplacement_by_slide_window(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        begin, end = 0, 0
        ans = 0
        max_char_count = 0
        char_count = {}

        for end in range(len(s)):
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            max_char_count = max(char_count.get(s[end]), max_char_count)

            # need to move the slide window forward if exceeds the k operation
            while (end - begin + 1) - max_char_count > k:
                char_count[s[begin]] -= 1
                begin += 1

            ans = max(ans, end - begin + 1)
        return ans


print(Solution().characterReplacement_by_slide_window("ABAAB", 2,))
print(Solution().characterReplacement("ABAAB", 2,))
