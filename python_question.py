'''
Find a pair with the given sum in an array. Given an unsorted integer array, print a pair
with the given sum in it.
For example,
Input:
nums = [8, 7, 2, 5, 3, 1]
target = 10
Output:
Pair found (8, 2) or
Pair found (7, 3)
—
Input:
nums = [5, 2, 6, 8, 1, 9]
target = 12
Output: Pair not found.
'''
def pair_sum(nums,target):
    a=[]
    for i in range(len(nums)):
        for j in range((i+1),len(nums)):
            if nums[j]+nums[i]==target: a.append((nums[i],nums[j]))
    return f"Pair found {a}"  if len(a) > 0 else "Pair not found."
        
print(pair_sum([8, 7, 2, 5, 3, 1],10))
print(pair_sum([5, 2, 6, 8, 1, 9],12))
    