# Python Function Tutorial

# 1. **Basic Function: Mean Calculation**

# Function to calculate the mean of a list of numbers
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

# Example usage
print(mean([10, 15, 17, 18, 13, 19]))  # Output: Mean of the list

# If a function has no return, it defaults to returning None.
# Avoid using print inside functions unless necessary as it prints the result + None.

# 2. **Function with Default and Non-Default Parameters**

# Function with default parameter value
def example(a, b=3):  # 'a' is a required parameter, 'b' defaults to 3
    return a * b

# Example usage
print(example(b=2, a=5))  # b is modified, a is 5
print(example(2))          # Uses default value for b
print(example(5, 2))       # a is 5, b is 2

# 3. **Arbitrary Number of Non-Keyword Arguments (args)**

# Function that accepts arbitrary number of non-keyword arguments
def mean4(*args):
    return args  # Returns a tuple of all the arguments

# Example usage
print(mean4(1, 2, 3, 'e', 5))  # Output: (1, 2, 3, 'e', 5)

# 4. **Arbitrary Number of Keyword Arguments (kwargs)**

# Function that accepts arbitrary number of keyword arguments
def mean3(**kwargs):
    return kwargs  # Returns a dictionary of keyword arguments

# Example usage
print(mean3(a=2, b=1, c='d'))  # Output: {'a': 2, 'b': 1, 'c': 'd'}

# *args and **kwargs are useful when you don’t know the exact number of arguments you’ll need in a function.

# 5. **Order Food Example**

# Function using *args (non-keyword arguments)
def order_food(*args):
    for item in args:
        print(f"Ordered {item}")

# Example usage
order_food("Pizza", "Fries", "Salad", "Burger", "Pasta")  # Prints each ordered item

# Function using **kwargs (keyword arguments)
def order_food_v2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
order_food_v2(pizza="Cheese", fries="Spicy", salad="Caesar", drink="Cola")  # Prints each key-value pair

# 6. **Conditionals with Functions**

# Function that calculates mean, checking if the input is a dictionary or list
def mean2(value):
    if isinstance(value, dict):  # Using isinstance for type checking
        the_mean = sum(value.values()) / len(value)  # Mean of dictionary values
    else:
        the_mean = sum(value) / len(value)  # Mean of list or other iterable
    return the_mean

# Example usage with a dictionary
dic = {"John": 15, "Doe": 17}
print(mean2(dic))  # Output: Mean of dictionary values (16)
