import os

# Set the directory path and file extension to search for
directory_path = "/home/nelly/Downloads"
file_extension = ".txt"
matching_files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

# Find all files with the specified extension in the directory


# Print the matching files
print("Matching files:")
for file in matching_files:
    print(os.path.join(directory_path, file))

# Ask the user if they want to delete the files
confirm = input("Do you want to delete these files? (y/n)")

if confirm == "y":
    # Delete the files
    for file in matching_files:
        os.remove(os.path.join(directory_path, file))
    print("Files deleted successfully.")
else:
    print("No files were deleted.")
