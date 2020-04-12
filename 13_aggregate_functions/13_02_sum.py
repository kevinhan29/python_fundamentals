'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

x = [1, 3, 5, 9, 10]
print(sum(x))