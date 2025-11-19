def countEvenNumbers(digits):
    digits = list(map(int, digits))  # convert strings to int if needed
    result = set()

    n = len(digits)

    for i in range(n):         # first digit
        for j in range(n):     # second digit
            for k in range(n): # third digit
                
                a, b, c = digits[i], digits[j], digits[k]

                # rule 1: first digit cannot be zero
                if a == 0:
                    continue

                # rule 2: last digit must be even
                if c % 2 != 0:
                    continue

                # check digit usage
                num_list = [a, b, c]

                ok = True
                for x in set(num_list):
                    if num_list.count(x) > digits.count(x):
                        ok = False
                        break

                if ok:
                    result.add(a*100 + b*10 + c)

    return len(result)
print(countEvenNumbers([1,2,3,4]))
