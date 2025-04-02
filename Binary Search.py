nums = input().strip()  # Read input as a string
nums = nums.strip("[]")  # Remove square brackets
nums = list(map(int, nums.split(",")))  # Convert to a list of integers


# Input: 5 2 8 1 3
flag=False
target=int(input())
for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]  # Swap
    
for i in range(len(nums)):
    if nums[i]==target:
        flag=True
if flag==True:
    print(i)
else:
    print(-1)


"""
class Solution:
    def search(self, nums, target):
        # Bubble Sort (your original)
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        # Fixed search with flag (your style)
        flag = False
        found_index = -1  # To remember where we found it
        for i in range(len(nums)):
            if nums[i] == target:
                flag = True
                found_index = i  # Store the correct index
                break  # Stop after first match
        
        if flag:
            return found_index
        else:
            return -1

# Test
solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))  # Output: 4 (correct)
print(solution.search([1,3,5,7], 8))  # Output: -1 (correct)

"""
