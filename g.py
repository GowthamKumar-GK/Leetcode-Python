from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp_nums1 = nums1[:m]  # copy the non-zero elements of nums1
        p1 = 0
        p2 = 0

        for p in range(n + m):
            if p2 >= n or (p1 < m and tmp_nums1[p1] <= nums2[p2]):
                nums1[p] = tmp_nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


# ---------- INPUT ----------
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# ---------- CALL FUNCTION ----------
Solution().merge(nums1, m, nums2, n)

# ---------- OUTPUT ----------
print(nums1)
