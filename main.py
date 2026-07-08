from food_order import calculate_total

def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
        
        # Call the external function to calculate total
        total = calculate_total(price, quantity)
        
        # Check if the calculation returned a validation error message
        if isinstance(total, str):
            print(f"Error: {total}")
        else:
            print(f"Total Payment = RM {total:.2f}")
            
    except ValueError:
        print("Error: Invalid input type. Please enter numerical values.")

if __name__ == "__main__":
    main()