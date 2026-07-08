def calculate_total(price, quantity):
    # Validate customer input
    if price <= 0:
        return "invalid price"
    if quantity <= 0:
        return "invalid quantity"
    
    # Calculate total
    total = price * quantity
    return total