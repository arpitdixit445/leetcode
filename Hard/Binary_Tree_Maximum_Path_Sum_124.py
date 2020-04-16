'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the
parent-child connections. The path must contain at least 
one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
'''

#Solution using DFS : Time O(n) Space O(n)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        arr = []
        self.helper(root,arr)
        if len(arr):
            return max(arr)
        return 0
    
    def helper(self,root,arr):
        if root is None:
            return 0
        left = self.helper(root.left,arr)
        right = self.helper(root.right,arr)
        val = left + right + root.val
        val2 = max([left+root.val,right+root.val,root.val])
        arr.append(max(val,val2))
        return val2