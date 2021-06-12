# DumperDuper
# A simple program for extract directory filenames
# Version 1.0
    
# Importing OS modules
import os
  
# Select Path
print("Inserit directory path: ")
path = input()

dirname = os.path.dirname(path)
dfire = os.listdir(path)

# Print the directory name  
print("Selected Directory: ", dirname)
print()

# Print the filenames
print("Files in there: ")
 
with os.scandir(path) as dirs:
    for file in dirs:
        print(file.name)
print("\nSCAN COMPLETED!")