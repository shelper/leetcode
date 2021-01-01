class Solution:
    def tallestBillboard(self, rods):
        left_height = {0: 0}
        left_rods = {0: []}
        right_rods = {0: []}
        for r in rods:
            prev_left_height = left_height.copy()
            prev_left_rods = left_rods.copy()
            prev_right_rods = right_rods.copy()
            for s in prev_left_height.keys():
                # height[i] is the one side height when difference between two side is i
                if prev_left_height.get(s + r, 0) > prev_left_height[s] + r:
                    left_height[s + r] = prev_left_height.get(s + r, 0)
                    left_rods[s + r] = prev_left_rods.get(s + r, [])
                    right_rods[s + r] = prev_right_rods.get(s + r, [])
                else:
                    # only add rods (+r) to height for one side
                    left_height[s + r] = prev_left_height[s] + r
                    left_rods[s + r] = prev_left_rods[s] + [r]
                    right_rods[s + r] = prev_right_rods[s]

                if prev_left_height.get(s - r, 0) > prev_left_height[s]:
                    # if the rod is for other side (-r), do not add it to height
                    left_height[s - r] = prev_left_height.get(s - r, 0)
                    left_rods[s - r] = prev_left_rods.get(s - r, [])
                    right_rods[s - r] = prev_right_rods.get(s - r, [])
                else:
                    left_height[s - r] = prev_left_height[s]
                    left_rods[s - r] = prev_left_rods[s]
                    right_rods[s - r] = prev_right_rods[s] + [-r]

        return left_height[0], left_rods[0], right_rods[0]


# test
a, b, c = Solution().tallestBillboard(list(range(1, 10)))
assert a == sum(b) == -sum(c)
