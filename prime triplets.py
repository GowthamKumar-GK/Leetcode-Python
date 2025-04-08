def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1
    for _ in range(T):
        N = int(data[ptr])
        ptr += 1
        arr = list(map(int, data[ptr:ptr + N]))
        ptr += N
        
        count = 0
        # Iterate all possible triplets i < j < k
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    product = arr[i] * arr[j] * arr[k]
                    if is_prime(product):
                        count += 1
        print(count)

solve()
