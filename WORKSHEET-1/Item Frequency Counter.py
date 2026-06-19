def count_items(items_list):
    
    counts = {}

    for item in items_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


# Test cases

# Product sales example
sales = ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Laptop"]
print(count_items(sales))

# Word frequency example
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_items(words))

# Empty list example
print(count_items([]))