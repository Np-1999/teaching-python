def generate_table():
    print("--- Opening simulated server connection ---")
    
    # 1. TODO: Add a 'try' block starting here
    
    user_input = input("Enter a number: ")
    num = int(user_input) # This line will throw an error if the input is text
    
    print(f"Multiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
        
    return "Table generated successfully" # The function exits here on success
    
    # 2. TODO: Add an 'except' block to catch a ValueError
    # Hint: This handles the scenario where the user types a string instead of a number.
    # Print a message like "Invalid input: Please enter a valid integer."
    # Return "Failed due to ValueError"
    
    # 3. TODO: Add a generic 'except Exception as e' block 
    # Hint: This is useful as a fallback to catch any other unexpected errors.
    # Print f"Sorry, some error occurred: {e}" and return "Failed due to unknown error".
    
    # 4. TODO: Add a 'finally' block
    # Hint: This block must execute even after the 'return' statements above.
    # Print "--- Closing simulated server connection ---"

# Run the function and print the final return value
status = generate_table()
print(f"Final Status: {status}")
