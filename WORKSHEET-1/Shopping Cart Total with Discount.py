def calculate_total(prices, discount_percent=0):
    
    subtotal = sum(prices)
    discount_amount = subtotal * (discount_percent / 100)
    final_total = subtotal - discount_amount

    return {
        "subtotal": round(subtotal, 2),
        "discount_amount": round(discount_amount, 2),
        "final_total": round(final_total, 2)
    }


# Test cases
print(calculate_total([10.99, 5.50, 3.25]))
print(calculate_total([10.99, 5.50, 3.25], 10))
print(calculate_total([100, 50, 25], 20))
print(calculate_total([]))