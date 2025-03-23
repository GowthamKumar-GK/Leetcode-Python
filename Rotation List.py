t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    # Read the array
    arr = list(map(int, input().split()))
    
    # Handle cases where k > n
    k = k % n  

    # Rotate the array
    rotated_arr = arr[-k:] + arr[:-k]

    # Print the result
    print(*rotated_arr)
