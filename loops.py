# Python Looping Concepts

# 1. **For Loop**

# Syntax for a basic for loop
# Example: Iterating over a range of numbers
for i in range(5):
    print(f"Iteration {i}")  # Output: Iterates over 0, 1, 2, 3, 4

# 2. **While Loop**

# Syntax for a basic while loop
# Example: Loop until a condition is met
a = 5
while a > 0:  # Loop runs while a is greater than 0
    print(f"Value of a: {a}")
    a -= 1  # Decrement a by 1 each time

# 3. **User Input with While Loop**

# Using a while loop to repeatedly prompt for user input
username = ''
while username != "pypy":  # Loop continues until the username is "pypy"
    username = input("Enter your username: ")
    # Loop finishes when the username is 'pypy'

# 4. **Infinite Loop with `while True`**

# Infinite loop (use carefully to avoid system freeze or excessive processing)
# It will keep running indefinitely until explicitly stopped with 'break'
while True:
    username = input("Enter your username: ")
    if username == 'pypy':
        print("Welcome, pypy!")
        break  # Exit the loop when the username is 'pypy'
    else:
        print("Try again.")  # Skip to the next iteration without breaking

# 5. **`break` and `continue` Statements**

# The `break` statement exits the loop immediately
# The `continue` statement skips the current iteration and moves to the next one

# Example of using 'break' and 'continue' within a loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(f"Iteration {i}")

# Example of using 'continue' within a loop
for i in range(5):
    if i == 2:
        continue  # Skip this iteration when i equals 2
    print(f"Iteration {i}")
