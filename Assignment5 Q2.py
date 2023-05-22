start = int(input("Enter the starting number of range: "))
end = int(input("Enter the ending number of range: "))
divisor = int(input("Enter the number to check for divisibility: "))

print("Numbers divisible by", divisor, "in the range", start, "to", end, "are:")
for i in range(start, end+1):
    if i % divisor == 0:
        print(i)