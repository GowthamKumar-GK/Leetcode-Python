def largest_number_after_k_removals(N, K):
    digits = list(N)
    window_size = len(digits) - K
    result = []
    start = 0
    
    for i in range(window_size):
        max_digit = '0'
        max_index = start
        # Find the maximum digit in the current window
        for j in range(start, len(digits) - (window_size - i - 1)):
            if digits[j] > max_digit:
                max_digit = digits[j]
                max_index = j
        result.append(max_digit)
        start = max_index + 1
    
    # Handle leading zeros
    result_str = ''.join(result).lstrip('0')
    return result_str if result_str else '0'

# Read input
N = input().strip()
K = int(input())

print(largest_number_after_k_removals(N, K))
