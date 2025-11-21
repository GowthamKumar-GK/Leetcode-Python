def majorityElement(nums):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # return the element with max frequency
    return max(counts, key=counts.get)

n = [2, 3, 4, 3, 3, 2, 2, 2]
print(majorityElement(n))

