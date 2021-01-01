class Solution(object):
    def ip_restore_recursive(self, s: str):
        total_seg_num = 4
        seg_ends = [0] * total_seg_num
        ips = []
        len_s = len(s)

        def dfs(seg_start, seg_idx):
            # not enough string for segmentation
            if len_s - seg_start < total_seg_num - seg_idx:
                return

            if seg_idx < total_seg_num - 1:  # last segment
                if s[seg_start] == "0":
                    max_seg_width = 1
                elif ord(s[seg_start]) > ord("2"):
                    max_seg_width = 2
                else:
                    max_seg_width = 3

                for seg_width in range(1, max_seg_width + 1):
                    seg_end = seg_start + seg_width
                    if int(s[seg_start:seg_end]) > 255:
                        return
                    else:
                        seg_ends[seg_idx] = seg_end
                        dfs(seg_end, seg_idx + 1)
            else:
                if s[seg_start] == "0" and len_s - seg_start > 1:  # last seg width > 1
                    return
                # last segment must be < 255
                if int(s[seg_start:]) > 255:
                    return
                # use rest of the string as last segment
                seg_ends[-1] = len_s
                seg_starts = [0] + seg_ends[:-1]
                ips.append(
                    ".".join(s[start:end] for start, end in zip(seg_starts, seg_ends))
                )
                return

        dfs(0, 0)
        return ips

    def ip_restore_deque(self, s: str):
        total_seg_num = 4
        if s[0] =='0':
            seg_steps = [(0, 1)]
        else:
            seg_steps =  [(0, 1), (0, 2), (0, 3)]
        
        for step in seg_steps:
            
            

        q = [1, 2, 3]
        seg_ends = [0] * total_seg_num
        ips = []
        len_s = len(s)


s = "0255200252"
print(Solution().ip_restore_recursive(s))
print(Solution().ip_restore_deque(s))
