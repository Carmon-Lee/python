# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        root1leaf = []
        root2leaf = []

        def scanleaf(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            scanleaf(root.left, leaves)
            scanleaf(root.right, leaves)

        scanleaf(root1, root1leaf)
        scanleaf(root2, root2leaf)
        if len(root1leaf) != len(root2leaf):
            return False
        if sum([abs(root1leaf[i] - root2leaf[i]) for i in range(len(root1leaf))]) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node2.right = node4

    print(s.leafSimilar(node1, node1))
