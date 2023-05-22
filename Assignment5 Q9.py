# Taking input from user
word_list = input("Enter a list of words separated by spaces: ").split()

# Counting occurrences of each word
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Printing the results
print("Number of times each word occurs:", word_count)