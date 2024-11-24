import math

def add_with_uncertainty(a, da, b, db):
    """Addition with uncertainties."""
    result = a + b
    uncertainty = math.sqrt(da**2 + db**2)
    return result, uncertainty

def subtract_with_uncertainty(a, da, b, db):
    """Subtraction with uncertainties."""
    result = a - b
    uncertainty = math.sqrt(da**2 + db**2)
    return result, uncertainty

def multiply_with_uncertainty(a, da, b, db):
    """Multiplication with uncertainties."""
    result = a * b
    uncertainty = result * math.sqrt((da / a)**2 + (db / b)**2)
    return result, uncertainty

def divide_with_uncertainty(a, da, b, db):
    """Division with uncertainties."""
    result = a / b
    uncertainty = result * math.sqrt((da / a)**2 + (db / b)**2)
    return result, uncertainty

def power_with_uncertainty(a, da, n):
    """Exponentiation with uncertainties."""
    result = a**n
    uncertainty = result * abs(n) * (da / a)
    return result, uncertainty

def multiply_by_constant(a, da, k):
    """Multiplication with a constant and uncertainty."""
    result = k * a
    uncertainty = abs(k) * da
    return result, uncertainty

def divide_by_constant(a, da, k):
    """Division by a constant and uncertainty."""
    result = a / k
    uncertainty = da / abs(k)
    return result, uncertainty

def custom1(A, dA, B, dB, k, n, m):
    """Computes Z = k * A^n / B^m with propagated uncertainties."""
    # Calculate Z
    Z = k * (A ** n) / (B ** m)
    
    # Calculate the uncertainty using the propagation formula for powers and division
    dZ = Z * math.sqrt((n * dA / A) ** 2 + (m * dB / B) ** 2)
    
    return Z, dZ




def main():
    print("Physics Uncertainty Calculator")
    print("Choose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Power")
    print("6: Multiplying by a constant")
    print("7: Dividing by a constant")
    print("8: Z = k * A^n/B^m")
    
    choice = input("Enter the number of the operation: ")
    
    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter the first value: "))
        da = float(input("Enter the uncertainty in the first value: "))
        b = float(input("Enter the second value: "))
        db = float(input("Enter the uncertainty in the second value: "))
        
        if choice == '1':
            result, uncertainty = add_with_uncertainty(a, da, b, db)
            operation = "addition"
        elif choice == '2':
            result, uncertainty = subtract_with_uncertainty(a, da, b, db)
            operation = "subtraction"
        elif choice == '3':
            result, uncertainty = multiply_with_uncertainty(a, da, b, db)
            operation = "multiplication"
        elif choice == '4':
            result, uncertainty = divide_with_uncertainty(a, da, b, db)
            operation = "division"
    
    elif choice == '5':
        a = float(input("Enter the value A: "))
        da = float(input("Enter the uncertainty in the value: "))
        n = float(input("Enter the power: "))
        result, uncertainty = power_with_uncertainty(a, da, n)
        operation = "exponentiation"
        
    elif choice == '6':  # Example: Multiplying by a constant
        a = float(input("Enter the value of A: "))
        da = float(input("Enter the uncertainty in the value: "))
        k = float(input("Enter the constant: "))
        result, uncertainty = multiply_by_constant(a, da, k)
        operation = "multiplication by a constant"
    
    elif choice == '7':  # Example: Division by a constant
        a = float(input("Enter the value of A: "))
        da = float(input("Enter the uncertainty in the value: "))
        k = float(input("Enter the constant: "))
        result, uncertainty = divide_by_constant(a, da, k)
        operation = "division by a constant"
        
    elif choice == '8':  # Example: k* A**n/B**m
        a = float(input("Enter the first value: "))
        n = float(input("Enter the power for the first value:"))
        da = float(input("Enter the uncertainty in the first value: "))
        b = float(input("Enter the second value: "))
        m = float(input("Enter the power for the second value:"))
        db = float(input("Enter the uncertainty in the second value: "))
        k = float(input("Enter the constant: "))
        result, uncertainty = custom1(a, da, b, db, k, n, m)
        operation = "k* A**n/B**m"
    
    else:
        print("Invalid choice!")
        return
    
    print(f"The result of the {operation} is: {result:.5f}")
    print(f"The uncertainty is: ±{uncertainty:.5f}")

if __name__ == "__main__":
    main()