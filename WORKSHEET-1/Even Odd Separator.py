def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:  # Even number
            even_numbers.append(num)
        else:  # Odd number
            odd_numbers.append(num)

    return even_numbers, odd_numbers


# Test cases
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens, odds = separate_even_odd(numbers)

print("Even numbers:", evens)
print("Odd numbers:", odds)

# Additional test
print(separate_even_odd([12, 15, 18, 21, 24]))
print(separate_even_odd([]))