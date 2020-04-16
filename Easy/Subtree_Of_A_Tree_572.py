'''
Given two non-empty binary trees s and t, check whether tree t 
has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this 
node's descendants. The tree s could also be considered as a subtree
of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true
'''

#Solution Using DFS : Time O(n^2) Space O(n)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        arr1 = []
        self.helper(t,arr1)
        arr = [0]
        self.check(s,arr1,arr)
        return arr[0] == 1
             
    def check(self, root,arr1,arr):
        if root is None:
            return
        self.check(root.left,arr1,arr)
        
        temp = []
        self.helper(root,temp)
        if temp == arr1:
            arr[0] = 1
        self.check(root.right,arr1,arr)
        
    def helper(self, root, arr):
        if root is None:
            return
        self.helper(root.left,arr)
        arr.append(root.val)
        self.helper(root.right,arr)