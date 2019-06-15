# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 主要考察树的遍历
class Solution(object):
    def bfs(self, p, k, save_sets):
        if p == None:
            return False
        t = k - p.val
        if t not in save_sets:
            save_sets.add(p.val)
        else:
            return True
        return self.bfs(p.left, k, save_sets) or self.bfs(
            p.right, k, save_sets)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        save_sets = set()
        ret = self.bfs(root, k, save_sets)
        return ret
