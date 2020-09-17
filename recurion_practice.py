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