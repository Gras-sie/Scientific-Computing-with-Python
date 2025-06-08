"""
PYTHON NUMERICAL METHODS & BISECTION ALGORITHM CHEAT SHEET:

NUMERICAL METHODS:
- Techniques for finding approximate solutions to mathematical problems
- Often used when exact solutions are difficult or impossible
- Common types: root finding, integration, differentiation, optimization

BISECTION METHOD:
- Root-finding algorithm that repeatedly divides an interval in half
- Requirements:
  * Continuous function f(x)
  * Initial interval [a,b] where f(a) and f(b) have opposite signs
- Converges linearly: error reduced by half in each iteration

CONVERGENCE CRITERIA:
- Absolute error: |f(x)| < tolerance
- Relative error: |x_new - x_old| / |x_new| < tolerance
- Maximum iterations: Prevent infinite loops

ERROR HANDLING:
- ValueError for invalid inputs
- Edge cases handling (e.g., square root of negative numbers)
- Special case handling (e.g., square root of 0 or 1)

FUNCTION PARAMETERS:
- Default parameters: function(param=default_value)
- Named arguments: function(param1=value1, param2=value2)
- Documenting parameters with docstrings

MATHEMATICAL OPERATIONS:
- Exponentiation: x**y (x raised to power y)
- Absolute value: abs(x)
- Maximum value: max(a, b)
- Comparison operators: <, >, <=, >=, ==, !=

ITERATION TECHNIQUES:
- for _ in range(n): Run loop n times
- break statement: Exit loop early
- continue statement: Skip to next iteration

PRECISION & FLOATING POINT:
- Scientific notation: 1e-7 equals 0.0000001
- Floating-point precision issues
- Avoiding division by zero
- Handling numerical stability
"""

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Check if input is negative - square roots of negative numbers are not real
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    # Handle special cases for 1 and 0
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Initialize the search interval
        low = 0  # Lower bound starts at 0
        high = max(1, square_target)  # Upper bound is at least 1 or the target number
        root = None
        
        # Bisection method iteration
        for _ in range(max_iterations):
            # Calculate midpoint of current interval
            mid = (low + high) / 2
            # Calculate square of midpoint
            square_mid = mid**2

            # Check if we've found a close enough answer
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            # If mid point is too small, adjust lower bound
            elif square_mid < square_target:
                low = mid
            # If mid point is too large, adjust upper bound
            else:
                high = mid

        # Check if we failed to find a solution within max iterations
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

# Example usage: find square root of 16
N = 16
square_root_bisection(N)