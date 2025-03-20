#HACKEARTH MAX SUM PROBLEM


def Max(arr):
    n = len(arr)
    Maxsum = float('-inf')

    for i in range(n):  # Start index
        specialsum = 0
        j = i
        k = 1  # Number of elements to pick in the current group

        while j + k <= n:  # Ensure we don't go out of bounds
            specialsum += sum(arr[j:j + k])  # Add the current group sum
            j += k  # Move to the next group
            k += 1  # Increase the group size

        Maxsum = max(Maxsum, specialsum)  # Keep track of max special sum

    return Maxsum

# Input Handling
n = int(input().strip())
arr = list(map(int, input().split()))

# Output the maximum special sum
print(Max(arr))
