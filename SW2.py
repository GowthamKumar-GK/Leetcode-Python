def maxVowels(s, k):
    l = 0
    r = k
    e = 0
    c = 0

    # Process the first window
    n = s[l:r]
    for i in n:
        if i in 'aeiou':
            c += 1
    e = c

    # Slide the window
    while r < len(s):
        if s[l] in 'aeiou':
            c -= 1
        if s[r] in 'aeiou':
            c += 1
        e = max(e, c)
        l += 1
        r += 1

    return e

# ----------- Input from user -----------
s = input("Enter the string: ")
k = int(input("Enter the window size (k): "))

# ----------- Output -----------
print("Maximum number of vowels in any substring of length k:", maxVowels(s, k))
