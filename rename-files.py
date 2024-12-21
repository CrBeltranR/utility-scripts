import os

"""
    File: renamer.py
    
    Author: Cristian Alejandro Beltran Rojas
    
    Date: 2024-12-21
    
    Description:
        This script renames all image and video files in a specified folder.
        Images are renamed to "Image_i" and videos to "Video_i", where "i" is
        a sequential counter. Supported image formats include JPG, PNG, GIF, etc.
        Supported video formats include MP4, AVI, MKV, etc.
    
    Version: 1.0

    Changelog: 
        - Initial version with support for renaming based on file type.
        - Optimized extension handling using a dictionary.
    
    Usage: 
        Run the script and provide the folder path when prompted.
"""

def rename_files(folder):
    # Check if the provided folder exists
    if not os.path.isdir(folder):
        print(f"The folder '{folder}' does not exist. Please check the path.")
        return

    # Define file types and their extensions
    # "Image" category includes common image file formats, including GIF
    # "Video" category includes common video file formats
    file_types = {
        "Image": ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'],
        "Video": ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    }

    # Initialize counters for each file type
    counters = {"Image": 1, "Video": 1}

    # Iterate through all files in the folder
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)  # Get the full path of the file
        
        if os.path.isfile(full_path):  # Check if it's a file, not a directory
            ext = os.path.splitext(file)[1].lower()  # Extract the file extension (in lowercase)
            
            # Check the file type by comparing the extension
            for file_type, extensions in file_types.items():
                if ext in extensions:  # If the extension matches a file type
                    # Generate the new name based on the file type and current counter
                    new_name = f"{file_type}_{counters[file_type]}{ext}"
                    counters[file_type] += 1  # Increment the counter for that file type
                    
                    # Rename the file to the new name
                    os.rename(full_path, os.path.join(folder, new_name))
                    print(f"Renamed: {file} -> {new_name}")  # Output the renaming process
                    break  # Exit the inner loop after renaming

    # Print completion message after all files are processed
    print("Renaming process completed.")

if __name__ == "__main__":
    # Entry point: Ask the user to input the folder path
    folder = input("Enter the folder path: ")
    rename_files(folder)
