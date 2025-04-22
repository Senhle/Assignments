# File Handling and Exception Handling Assignment

# Ask the user for a filename to read
filename = input("Enter the name of the file to read: ")

try:
    # Try to open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
        print("\nOriginal Content:")
        print(content)

        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Save the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"\nModified content saved to {new_filename}")

except FileNotFoundError:
    print("\nError: The file you entered does not exist.")
except IOError:
    print("\nError: There was a problem reading or writing the file.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
