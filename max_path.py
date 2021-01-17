class Tree:
    def __init__(self, tree_data) -> None:
        super().__init__()
        self.root = Node(tree_data[0])
        for data in tree_data[1:]:
            self.root.add_child(data)

    def __repr__(self) -> str:
        s = [[] for i in range(4)]

        def output(node, level):
            s[level].append(node.val)
            if node.left is not None:
                output(node.left, level + 1)
            if node.right is not None:
                output(node.right, level + 1)

        output(self.root, 0)
        return "\n".join([" ".join([str(v) for v in t]) for t in s])


class Node:
    def __init__(self, val) -> None:
        super().__init__()
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, child_val):
        if self.left is None:
            self.left = Node(child_val)
        elif self.right is None:
            self.right = Node(child_val)
        elif self.left.right is None:
            self.left.add_child(child_val)
        else:
            self.right.add_child(child_val)


class Solution:
    def __init__(self, tree_data) -> None:
        super().__init__()
        self.tree = Tree(tree_data)
        self.max_path = float("-inf")

    def get_max_path(self):
        def max_sub_path(node):
            if node is None:
                return 0
            else:
                left_max = max(max_sub_path(node.left) + node.val, 0)
                right_max = max(max_sub_path(node.right) + node.val, 0)

                self.max_path = max(self.max_path, left_max + node.val + right_max)
                # Should've used the line below, but because we set the minimum to 0 as above, we can simplify to the line above
                # self.max_path = max(self.max_path, left_max + node.val + right_max, left_max, right_max)
                return max(left_max, right_max)

        max_sub_path(self.tree.root)
        return self.max_path


tree_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tree = Tree(tree_data)
print(tree)

s = Solution(tree_data)
print(s.get_max_path())
