class Solution(object):
    def ip_restore_recursive(self, s: str):
        total_seg_num = 4
        seg_ends = [0] * total_seg_num
        ips = []
        len_s = len(s)

        if len_s < 4:
            return

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

    def ip_restore_queue(self, s: str):
        total_seg_num = 4
        ips = []
        len_s = len(s)
        seg_ends = [0] * (total_seg_num + 1)

        if len_s < 4:
            return

        segs = [(-1, 0)]  # list of segs as (seg_id, seg_end_idx)

        while len(segs) > 0:
            seg = segs.pop()
            seg_ends[seg[0] + 1] = seg[1]
            if seg[0] == 3:
                if seg[1] == len_s:
                    ips.append(
                        ".".join(
                            s[start:end]
                            for start, end in zip(seg_ends[:-1], seg_ends[1:])
                        )
                    )
            else:
                next_seg_idx = seg[0] + 1
                next_seg_start = seg[1]  # new seg starts at the end of previous seg
                if next_seg_start >= len_s:
                    continue
                if s[next_seg_start] == "0":
                    next_seg = (next_seg_idx, next_seg_start + 1)
                    if next_seg[0] == 3 and next_seg[1] == len_s:
                        continue
                    segs.append(next_seg)
                else:
                    for i in range(1, min(len_s - next_seg_start + 1, 4)):
                        next_seg = (next_seg_idx, next_seg_start + i)
                        if int(s[seg[1] : next_seg[1]]) > 255:
                            break
                        segs.append(next_seg)

        return ips


s = "025520252"
print(Solution().ip_restore_recursive(s))
print(Solution().ip_restore_queue(s))
