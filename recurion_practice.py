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