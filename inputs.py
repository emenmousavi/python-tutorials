# Python User Input and String Handling

# 1. **Weather Condition Function**
# Function to check the weather based on the temperature
def weather_condition(temp):
    if temp > 7:
        return "warm"  # Return 'warm' if the temperature is above 7
    else:
        return "cold"  # Return 'cold' if the temperature is 7 or lower

# Example usage: Uncomment the following lines to test the function with user input
# user_input = int(input("Enter the temperature: "))  # Take the temperature as input
# print(weather_condition(user_input))  # Print the weather condition based on the input

# 2. **User Input Functionality**

# Basic usage of `input()` function
# input() is used to get input from the user, and it returns data as a string

# Example of a simple user input:
# input("Enter something: ")

# 3. **Type Conversion for Input**

# You can convert the user input to a specific data type using `int()`, `float()`, etc.
# Example: Converting user input to an integer
# int(input("Enter a number: "))  # Convert the input to an integer before using it

# 4. **String Formatting with User Input**

# 4.1 **Concatenation**
# Using concatenation to combine user input into a message
name = input("Enter your name: ")
message = "Hello " + name  # Concatenate the string with the user input
print(message)

# 4.2 **Old-style String Formatting**
# Using the old version of string formatting with the `%` operator
message2 = "Hello %s" % name  # This is the older way to format strings
print(message2)

# 4.3 **Newer f-String Formatting (Python 3.7+)**
# Using f-string (available since Python 3.6) for better readability and efficiency
message3 = f"Hello {name}"  # f-string is a modern and cleaner approach
print(message3)

# 5. **Multiple User Inputs**
# Accepting multiple pieces of user input for use in variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Concatenation of multiple inputs
message = "My name is " + name + " " + surname
print(message)

# 5.1 **Alternative String Formatting (f-string)**
# Another way to combine multiple inputs using f-string
message2 = f"My name is {name} {surname}"  # Cleaner and more readable
print(message2)
