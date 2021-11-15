# Binary search function using recursion
def binary_search(arr, low, high, x):
    # Base case when we are left with only the high and low indices. When we calculate mid and try to run the function
    # again, the low and high indices will cross with the addition of 1 to low, or subtraction of 1 from high.
    if low > high:
        print('Not found')
        return -1

    # Calculate the middle index using integer division
    mid = (high + low) // 2

    # See if x is in the middle, if not, determine if x is in the left or right half of the array
    if arr[mid] == x:
        print('Found!')
        return 0
    elif arr[mid] > x:  # In left half
        binary_search(arr, low, mid-1, x)
    elif arr[mid] < x:  # In right half
        binary_search(arr, mid+1, high, x)
    else:
        print('Something went wrong')
        return -2


# Hardcoded array for quick testing, must be sorted for binary search to work
arr = [-7, 0, 1, 2, 5, 8, 10, 13, 40, 55]
arr_max_index = len(arr) - 1
low_num = arr[0]
high_num = arr[arr_max_index]

# Get user input for integer to search for, making sure they enter an integer in range of the array
while True:
    x = input(f'Enter an integer to search for in the range ({low_num} - {high_num}): ')
    if x.lstrip('-').isdigit() and low_num <= int(x) <= high_num:
        x = int(x)
        break
    else:
        print(f'Please enter an integer in the range {low_num} - {high_num}.\n')

# Run the search function
binary_search(arr, 0, arr_max_index, x)
