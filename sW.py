from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = n + 1  # sentinel (larger than any possible subarray)

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                # update minimal length
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len

                # shrink from left
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == n + 1 else min_len


# Example driver code
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))    # expected 2
    print(sol.minSubArrayLen(4, [1,4,4]))          # expected 1
    print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # expected 0
