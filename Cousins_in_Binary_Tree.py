'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.


Example 1 :
[Example 1 Link] (https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Exaple 2:
<a href="https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png">Example 2 Link</a>
[Example 2 Link] (https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
[Example 2 Link] (https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        curr = [root]
        while curr:
            xfound = False
            yfound = False
            for n in curr:
                if n.val==x:
                    xfound = True
                if n.val==y:
                    yfound = True
            if xfound and yfound:
                return True
            if xfound or yfound:
                return False
            ncurr = []
            for n in curr:
                if n and n.left and n.right and ((n.left.val==x and n.right.val==y) or (n.right.val==x and n.left.val==y)):
                    return False
                if n.left:
                    ncurr.append(n.left)
                if n.right:
                    ncurr.append(n.right)
            curr = ncurr
        return False
          
        
