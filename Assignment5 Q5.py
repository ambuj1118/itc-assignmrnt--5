rows = int(input("Enter the number of rows: "))
count = 65 # ASCII value of 'A'

for i in range(1, rows+1):
    for j in range(i):
        print(chr(count), end=" ")
        count += 1
        if count > 90: # If count exceeds ASCII value of 'Z'
            count = 65 # Reset count to 'A'
    print()