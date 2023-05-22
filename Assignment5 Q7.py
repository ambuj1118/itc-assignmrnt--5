print("Numbers which are multiple of 7 and divisible by 11 in the range 1-500 are: ")
for num in range(1, 501):
    if num % 7 == 0 and num % 11 == 0:
        print(num)