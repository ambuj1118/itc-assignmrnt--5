# Taking input from user
num_list = []
for i in range(10):
    num = int(input("Enter a number: "))
    num_list.append(num)

# Finding positive, negative, odd and even numbers
positive_nums = []
negative_nums = []
odd_nums = []
even_nums = []

for num in num_list:
    if num > 0:
        positive_nums.append(num)
    elif num < 0:
        negative_nums.append(num)
    
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

# Counting occurrences of each number
num_count = {}
for num in num_list:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

# Printing the results
print("Positive Numbers:", positive_nums)
print("Negative Numbers:", negative_nums)
print("Odd Numbers:", odd_nums)
print("Even Numbers:", even_nums)
print("Number of times each number occurs:", num_count)