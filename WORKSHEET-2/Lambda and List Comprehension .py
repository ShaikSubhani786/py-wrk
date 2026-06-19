numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. List comprehension to create a list of squares
squares = [num ** 2 for num in numbers]

# 2. Lambda function to create a list of even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original List:", numbers)
print("Squares List:", squares)
print("Even Numbers List:", even_numbers)