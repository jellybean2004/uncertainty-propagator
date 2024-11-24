import sympy as sp

# Function to get the function and its variables from the user
def get_function_and_variables():
    # Ask user for the function
    func_input = input("Enter the function (e.g., x**2 + 3*x + 2): ")
    
    # Convert the input string to a sympy expression
    function = sp.sympify(func_input)
    
    # Get the variables in the function
    symbols = list(function.free_symbols)
    
    # If no variables found, notify the user
    if not symbols:
        print("No variables were found in the function.")
        return None, None
    
    # Ask for uncertainties (errors) for each variable
    errors = []
    for var in symbols:
        error_input = input(f"Enter the uncertainty for {var}: ")
        errors.append(float(error_input))
    
    return function, list(zip(symbols, errors))

# Function to propagate errors based on the functional approach
def propagate_uncertainties(function, variables_with_errors):
    # Calculate partial derivatives and propagate the uncertainties
    total_uncertainty = 0
    for var, error in variables_with_errors:
        # Calculate the partial derivative with respect to the variable
        partial_derivative = sp.diff(function, var)
        # Add the square of the contribution from each variable's uncertainty
        total_uncertainty += (partial_derivative ** 2) * (error ** 2)
    
    # Return the square root of the total uncertainty
    return sp.sqrt(total_uncertainty)

# Function to evaluate the function and uncertainty at a specific point
def evaluate_at_point(function, uncertainty, values):
    # Substitute the values into the function and uncertainty expression
    evaluated_function = function.subs(values)
    evaluated_uncertainty = uncertainty.subs(values)
    
    return evaluated_function, evaluated_uncertainty

def main():
    # Get function and uncertainties from user
    function, variables_with_errors = get_function_and_variables()
    
    if function is None:
        return
    
    # Propagate the uncertainties
    uncertainty = propagate_uncertainties(function, variables_with_errors)
    
    # Ask the user for the point at which to evaluate
    values = {}
    for var, _ in variables_with_errors:
        value_input = input(f"Enter the value for {var}: ")
        values[var] = float(value_input)
    
    # Evaluate the function and uncertainty at the given point
    evaluated_function, evaluated_uncertainty = evaluate_at_point(function, uncertainty, values)
    
    # Output the result
    print(f"\nFunction: {function}")
    print(f"Propagated Uncertainty: {uncertainty}")
    print(f"Evaluated Function at {values}: {evaluated_function}")
    print(f"Evaluated Uncertainty at {values}: {evaluated_uncertainty}")

if __name__ == "__main__":
    main()