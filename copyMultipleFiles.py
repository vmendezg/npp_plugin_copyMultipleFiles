import os  # Standard library to extract the filename from the full path

# 1. Open the modal to request the file name
nombre_archivo = notepad.prompt("Enter the name for the combined file:", "Result", "Result.txt")

# If the user clicks 'Cancel' or leaves it empty, stop the script
if nombre_archivo is None or nombre_archivo.strip() == "":
    notepad.messageBox("Operation cancelled by the user.", "Notice")
else:
    # Save the current filename before creating the new one for comparison
    archivo_actual_antes = notepad.getCurrentFilename()
    
    # 2. Create the new file with the entered name
    notepad.new()
    
    # 3. Temporary list to store the formatted text from the other files
    textos_combinados = []

    # 4. Iterate through all open files
    for f in notepad.getFiles():
        # f is a tuple (path, id), we extract the path string using f[0]
        filename = f[0]
        
        # Avoid copying the new file we just created
        if filename != notepad.getCurrentFilename():
            notepad.activateFile(filename)
            
            # Extract only the short file name (e.g., "saluda.txt") from the full path
            short_name = os.path.basename(filename)
            
            # If it's an unsaved tab (like "new 1"), use a fallback name
            if not short_name:
                short_name = "Unsaved Tab"
                
            file_content = editor.getText()
            
            # Format: filename followed by its content on the next line
            formatted_block = short_name + "\n" + file_content
            textos_combinados.append(formatted_block)

    # 5. Return to the new file (extracting the path string with [0] from the last tuple) and paste everything
    notepad.activateFile(notepad.getFiles()[-1][0])
    
    # Join all blocks using a simple newline separator to match your exact format
    editor.setText("\n".join(textos_combinados))
    
    # Note: The file is created in Notepad++ with the combined text.
    # To save it physically to your drive with the chosen name, press Ctrl+S.
