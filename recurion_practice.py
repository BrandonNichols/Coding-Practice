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
        self.current_count = 0
        self.current_value = 0
        self.highest_count = 0
        
        def longPath(root):
            
            if root is None:
                return  
            
            if self.current_value == root.val:
                self.current_count += 1
                
                if self.highest_count < self.current_count:
                    self.highest_count = self.current_count
                    
            self.current_value = root.val
            longPath(root.left)
            longPath(root.right)
            
            return
        
        longPath(root)
        
        return self.highest_count