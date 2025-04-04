# Python Tutorial: Data Types, Functions, and Attributes

# 1. **Using Built-in Functions**
# - Use `help(function)` to learn more about a function in CLI
# - Use `dir(function)` to view all attributes of a function or variable

# 2. **Data Types**

# Integer
integer = 10

# String
string = "10"

# Float
floatt = 10.1

# 3. **List Operations**

# Creating a list
l = [10, 11, 12, 13, 14, 15]

# Use `dir(list)` to see all available list methods
# Example of string manipulation using `upper()` method
var1 = "Hello World!"
up = var1.upper()
print(up)  # Output: "HELLO WORLD!"

# List operations: Calculating average of list elements
countl = len(l)  # Length of the list
summerl = sum(l)  # Sum of the list elements
avel = summerl / countl  # Average value
print(f"Average of list elements: {avel}")

# 4. **Dictionary Operations**

# Creating a dictionary
dic = {"Marry": 11.5, "Ali": 15.6, "Inna": 18, "John": 17.5}

# Accessing dictionary attributes:
# .keys() for keys (e.g., "Marry")
# .values() for values (e.g., 11.5)
# .items() for key-value pairs (e.g., "Marry": 11.5)

# Calculating mean value of dictionary values
sumdic = sum(dic.values())  # Sum of dictionary values
lendic = len(dic)  # Length of dictionary
meandic = sumdic / lendic  # Mean value
print(f"Mean value of dictionary values: {meandic}")

# 5. **Tuple Operations**

# Creating a tuple
tup = (1, 5, 8)

# Note: Tuple is immutable, whereas lists are mutable (modifiable and can append elements)
# Convert tuple to list for modification, then convert it back to tuple (e.g., `li = list(tup)`)

# 6. **List Methods and Operations**

# Adding an element to the list
l.append(14)  # Append 14 to the list

# Remove the last element
l.pop()

# Reverse the list
l.reverse()

# Accessing and modifying elements in the list
print(f"Second element (rounded): {round(l[1])}")  # Round the second element

# Joining all list elements into a string
joined_str = ''.join(map(str, l))  # Ensure elements are strings before joining

# Accessing index of an element
print(f"Index of 14: {l.index(14)}")

# Accessing elements using index
print(f"Element at index 1: {l[1]}")  # Equivalent to l.__getitem__(1)

# Slicing the list
print(f"Elements from index 2 to 4: {l[2:4]}")  # List slice from index 2 to 4
print(f"Elements from index 0 to 3: {l[:3]}")  # List slice from index 0 to 3
print(f"Elements from index 3 to end: {l[2:]}")  # List slice from index 2 to the end
print(f"Last two elements: {l[-2:]}")  # Slice last two elements

# 7. **String Operations**

# String indexing and slicing
string2 = "This is an example"
print(f"Character at index 2: {string2[2]}")  # Output character at index 2
print(f"Substring from index 2 to the end: {string2[2:]}")  # Slice from index 2 to end

# Title case of string
print(f"Title case: {string2.title()}")  # Converts the first letter of each word to uppercase

# Accessing elements within lists of mixed data types
l2 = ['hello', 2, 5]
print(f"Character at index 3 in first list element: {l2[0][3]}")  # Access 3rd character in the first string element

# 8. **Dictionary Attribute Example**

# Accessing dictionary elements by key
print(f"Value for 'John': {dic['John']}")

# Adding new key-value pair to the dictionary
dic["Julie"] = 18  # Adds "Julie": 18 to the dictionary
print(f"Updated dictionary: {dic}")
