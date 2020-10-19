'''
This code practice section will be used to understand the idea behind recursion
'''

'''
Sum a list of numbers up to the value n using recursion
'''
def sum(arr, n):
    if n <= 0:
        return 0
    else:
        return sum(arr, n - 1) + arr[n - 1]

print(sum([1], 0)) #return 0
print(sum([2, 3, 4], 1)) #return 2
print(sum([2, 3, 4, 5], 3)) #return 9

'''
Longest Univalue Path
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
        
   def longestUnivaluePath(self, root):
        self.highest_count = 0
        self.current_count = 0
        self.start_traverse = True
        
        def longPath(root, previous_value = root.val):
            
            if root is None:
                return
            
            if not self.start_traverse:
                if previous_value == root.val:
                    self.current_count += 1
                    
                    if self.highest_count < self.current_count:
                        self.highest_count = self.current_count
                else:
                    self.current_count = 0
                    
                previous_value = root.value
            else:
                self.start_traverse = False
                    
            longPath(root.left, previous_value)
            longPath(root.right, previous_value)
            
            return
        
        longPath(root)
        
        return self.highest_count

'''
Range Sum of BST
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Understand:
Need to be able to recursively go down binary tree starting from left side to find L. When found return L and add and return only nodes that are between L and R while trying to reach R
'''

class Solution:
    def rangeSumBST(self, root, L, R):
        
        def rangeSumBSTHelper(root):
        
            if root is None:
                return

            if root.val == L:
                self.found_L = True

            if root.val == R:
                self.found_R = True
                self.sum_val += root.val

            if self.found_L:
                if root.val >= L and root.val <= R:
                    self.sum_val += root.val

            if not self.found_L and not self.found_R:
                rangeSumBSTHelper(root.left)
                rangeSumBSTHelper(root.right)
        
        self.sum_val = 0
        self.found_L = False
        self.found_R = False
        rangeSumBSTHelper(root)
        return self.sum_val