import os

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    
    # Create a new text file with the note title
    file_name = f"{title.lower().replace(' ', '_')}.txt"
    
    with open(file_name, 'w') as file:
        file.write(content)
    
    print(f"Note '{title}' saved successfully!")

def read_note():
    title = input("Enter note title to read: ")
    file_name = f"{title.lower().replace(' ', '_')}.txt"
    
    # Check if the note file exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"\nNote Title: {title}\n")
            print(content)
    else:
        print(f"Note '{title}' not found!")

def delete_note():
    title = input("Enter note title to delete: ")
    file_name = f"{title.lower().replace(' ', '_')}.txt"
    
    # Check if the note file exists
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Note '{title}' deleted successfully!")
    else:
        print(f"Note '{title}' not found!")

def main():
    while True:
        print("\n1. Create a new note")
        print("2. Read a note")
        print("3. Delete a note")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            create_note()
        elif choice == '2':
            read_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting the note program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
