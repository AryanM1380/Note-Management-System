# Note Management System

This simple Python script allows you to manage your notes. You can create, read, and delete notes through a command-line interface.

## Prerequisites
- Python 3.x installed on your system

## How to Use

1. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the command: `python script_name.py` (replace `script_name.py` with the actual name of the script).

2. **Options:**
   - You will be presented with the following options:
     - `1. Create a new note`
     - `2. Read a note`
     - `3. Delete a note`
     - `4. Exit`

3. **Creating a New Note:**
   - Choose option `1` to create a new note.
   - Enter the title and content for your note when prompted.
   - A text file will be created with the note title, and the content will be saved inside.

4. **Reading a Note:**
   - Choose option `2` to read a note.
   - Enter the title of the note you want to read.
   - If the note exists, its content will be displayed; otherwise, a message will indicate that the note was not found.

5. **Deleting a Note:**
   - Choose option `3` to delete a note.
   - Enter the title of the note you want to delete.
   - If the note exists, it will be deleted; otherwise, a message will indicate that the note was not found.

6. **Exiting the Program:**
   - Choose option `4` to exit the program. A goodbye message will be displayed, and the program will terminate.

## File Naming Convention
- Note files are saved with names based on the note title, converting to lowercase and replacing spaces with underscores.

## Example
```
1. Create a new note
2. Read a note
3. Delete a note
4. Exit
Enter your choice (1-4): 1
Enter note title: My First Note
Enter note content: This is the content of my first note.
Note 'My First Note' saved successfully!

1. Create a new note
2. Read a note
3. Delete a note
4. Exit
Enter your choice (1-4): 2
Enter note title to read: My First Note

Note Title: My First Note

This is the content of my first note.

1. Create a new note
2. Read a note
3. Delete a note
4. Exit
Enter your choice (1-4): 3
Enter note title to delete: My First Note
Note 'My First Note' deleted successfully!

1. Create a new note
2. Read a note
3. Delete a note
4. Exit
Enter your choice (1-4): 4
Exiting the note program. Goodbye!
```

Feel free to use and customize this script to fit your specific needs.
