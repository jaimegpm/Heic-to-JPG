import os
import re

def find_and_delete_duplicates():
    # Regular expression pattern for files ending with (1), (2), etc.
    pattern = r'.*\(\d+\)\..*$'
    
    # Get current directory
    current_dir = os.getcwd()
    
    # List to store files to be deleted
    duplicates = []
    
    # Find all duplicate files
    for filename in os.listdir(current_dir):
        if re.match(pattern, filename):
            duplicates.append(filename)
    
    if not duplicates:
        print("No duplicate files found.")
        return
    
    # Show files that will be deleted
    print("\nFound the following duplicate files:")
    for file in duplicates:
        print(f"- {file}")
    
    # Ask for confirmation
    confirm = input("\nDo you want to delete these files? (yes/no): ")
    
    if confirm.lower() == 'yes':
        # Delete the files
        for file in duplicates:
            try:
                file_path = os.path.join(current_dir, file)
                os.remove(file_path)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {str(e)}")
        print("\nDeletion complete!")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    find_and_delete_duplicates()

