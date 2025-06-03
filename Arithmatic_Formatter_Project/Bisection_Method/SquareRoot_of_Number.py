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