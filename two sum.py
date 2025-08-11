class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l, r]
            elif s < target:
                l += 1
            else:
                r -= 1

# ----------- USER INPUT SECTION -------------

# Get input list from user (comma-separated numbers)
nums_input = input("Enter sorted numbers separated by commas: ")
nums = list(map(int, nums_input.split(',')))

# Get target from user
target = int(input("Enter the target value: "))

# Create object and call function
sol = Solution()
result = sol.twoSum(nums, target)

# Print result
print("Indices of numbers that sum to target:", result)
