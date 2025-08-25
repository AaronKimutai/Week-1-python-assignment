# Open a file, read its content, modify it, and write to a new file
with open('aaron.txt', 'r') as file:
 content = file.read()

# Modify the content (for example, convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open('titus.txt', 'w') as file:
 file.write(modified_content)
 
print("File written successfully.")

# Prompt the user for a filename and display its content with error handling
filename = input("Enter filename: ")

try:
    with open(filename, 'r') as file:
     content= file.read()
    
    print("\n--- File Content ---\n")
    print(content)
    
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You do not have permission to read this file!")
except:
    print("Something went wrong while trying to open the file!")
    