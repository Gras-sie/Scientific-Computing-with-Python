def merge_sort(array):
    """
    Merge Sort Algorithm - A divide-and-conquer sorting algorithm
    
    The algorithm works by:
    1. Dividing the array into two halves
    2. Recursively sorting each half
    3. Merging the sorted halves back together
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    
    # Base case: Arrays with 1 or 0 elements are already sorted
    if len(array) <= 1:
        return
    
    # Step 1: Divide the array into two halves
    middle_point = len(array) // 2  # Find the middle index using integer division
    left_part = array[:middle_point]   # Left half: from start to middle (exclusive)
    right_part = array[middle_point:]  # Right half: from middle to end
    
    # Step 2: Recursively sort both halves
    # These calls will keep dividing until we reach single elements
    merge_sort(left_part)   # Sort the left half
    merge_sort(right_part)  # Sort the right half
    
    # Step 3: Merge the sorted halves back into the original array
    # Initialize pointers for tracking positions in each array
    left_array_index = 0   # Pointer for left_part array
    right_array_index = 0  # Pointer for right_part array
    sorted_index = 0       # Pointer for the main array being sorted
    
    # Main merge loop: Compare elements from both halves and place smaller one first
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Compare current elements from both halves
        if left_part[left_array_index] < right_part[right_array_index]:
            # Left element is smaller, place it in the sorted array
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1  # Move to next element in left array
        else:
            # Right element is smaller or equal, place it in the sorted array
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1  # Move to next element in right array
        
        sorted_index += 1  # Move to next position in the main array
    
    # Handle remaining elements: One array may have leftover elements
    
    # Copy any remaining elements from the left array
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copy any remaining elements from the right array
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# Test the merge sort algorithm
if __name__ == '__main__':
    # Create a sample unsorted array
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Display the original unsorted array
    print('Unsorted array: ')
    print(numbers)
    
    # Apply merge sort algorithm (sorts in-place)
    merge_sort(numbers)
    
    # Display the sorted result
    print('Sorted array: ' + str(numbers))