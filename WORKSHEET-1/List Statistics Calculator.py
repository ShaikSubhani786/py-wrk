def calculate_statistics(numbers):
    
    if not numbers:
        return {
            "error": "The list is empty."
        }

    return {
        "mean": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "count": len(numbers)
    }


# Test cases
print(calculate_statistics([10, 20, 30, 40, 50]))
print(calculate_statistics([5, 15, 25]))
print(calculate_statistics([]))