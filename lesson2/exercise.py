def fetch_element():
    my_list = [1,2,3,4]  # List with valid indices 0, 1, 2, 3
    
    # 1. TODO: Add a 'try' block starting here
    
    user_input = input("Enter the index: ")
    index = int(user_input)
    
    print(f"The value at index {index} is {my_list[index]}")
    return 1 # Returns 1 to indicate success
    
    # 2. TODO: Add an 'except' block to catch ValueError
    # Hint: This handles the case where the user inputs a string (e.g., "harry") instead of an integer.
    # Print "Invalid input: Please enter a number." and return 0.
    
    # 3. TODO: Add an 'except' block to catch IndexError
    # Hint: This handles the case where the user enters a number outside the list bounds (e.g., 5).
    # Print "Index out of bounds!" and return 0.
    
    # 4. TODO: Add a 'finally' block
    # Hint: Print "I am always executed!" 

# Run the function
result = fetch_element()
print(f"Function returned: {result}")