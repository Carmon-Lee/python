# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.doIsSymmetric(root,root)

    def doIsSymmetric(self, node1, node2):
        if (node1 and not node2) or (node2 and not node1):
            return False
        if node1 == node2:
            return True
        return node1.val == node2.val \
               and self.doIsSymmetric(node1.left, node2.right) \
               and self.doIsSymmetric(node1.right, node2.left)


if __name__ == '__main__':
    print(Solution().isSymmetric(TreeNode(3)))
