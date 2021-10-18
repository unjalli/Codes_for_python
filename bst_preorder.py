class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    
    def _createBST(self, preorder, max_val):
        print(preorder)
        print(max_val)
        if not preorder or preorder[-1]>max_val:
            return None
        root = TreeNode(preorder.pop())
        root.left = self._createBST(preorder, root.val)
        root.right = self._createBST(preorder, max_val)
        return root

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self._createBST(preorder[::-1], 10000)


preorder = [8, 5, 1, 7, 10, 12]
root = Solution().bstFromPreorder(preorder)
print(root)
