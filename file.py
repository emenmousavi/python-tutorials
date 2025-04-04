# Python File Handling

# 1. **Open and Read a File in the Same Path as the Python File**

# Open a file in the same directory as the script
myfile = open("file3.txt")

# Read content from the file (calling read() twice will give an empty result the second time)
content = myfile.read()  # Read the entire file content once
print(content)  # Print the content

# Close the file after usage to free up resources
myfile.close()

# **Important**: The cursor is at the end of the file after the first read, so the second call to read() will return an empty string.

# 2. **Using "with" for File Handling** (Automatically closes the file when done)

# Using "with" to open and automatically close the file after reading
with open("file3.txt") as myfile:
    content = myfile.read()  # Read the file content
print(content)  # Print the content

# 3. **Reading a File from a Different Path**

# Use raw string notation (r"") to ignore backslashes in the file path
with open(r"F:\Python Exercises\file2.txt") as myfile2:
    content2 = myfile2.read()  # Read the content of the file
print(content2)  # Print the content

# Alternatively, specify the read mode explicitly as "r"
with open(r"F:\Python Exercises\file2.txt", "r") as myfile2:
    content2 = myfile2.read()  # Read the content of the file
print(content2)  # Print the content

# 4. **Write to an Existing File (Overwrite the File)**

# Writing to a file, this will overwrite the file content
with open(r"F:\Python Exercises\file.txt", "w") as myfile3:
    myfile3.write("Spaceship ")
    myfile3.write("Garlic ")
    myfile3.write("Tomato\nCucumber\nOnion")

# Read the content of the file after writing to it
with open(r"F:\Python Exercises\file.txt", "r") as myfile3:
    content3 = myfile3.read()  # Read the content of the file
print(content3)  # Print the content

# 5. **Overwrite the File with New Content**

# Overwrite a file with new content (this is commented out but can be used if needed)
# with open(r"F:\Python Exercises\FILE.TXT", "w") as myfile2:
#     content2 = myfile2.write("FILENAME.TXT")

# 6. **Create a New File**

# Create a new file (if the file exists, this will raise an error, so use carefully)
# with open(r"F:\Python Exercises\file.txt", "x") as myfile3:
#     pass  # Placeholder for any operations

# 7. **Append to an Existing File**

# Open the file in append mode to add content without overwriting the existing data
with open(r"F:\Python Exercises\file.txt", "a+") as myfile4:
    myfile4.write("\nOkra")  # Add a new line with "Okra"
    myfile4.seek(0)  # Move the cursor to the beginning of the file
    content4 = myfile4.read()  # Read the entire content of the file from the start
print(content4)  # Print the content after appending
