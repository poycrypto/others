import zipfile
import os
import sys

# Ensure the working directory is the folder where the .exe is located
if getattr(sys, 'frozen', False):  # Check if the script is frozen as .exe
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the folder where the zip files are stored (same directory as the script or .exe)
zip_folder_path = script_dir
extract_folder_path = script_dir

# Create the extract folder if it does not exist
os.makedirs(extract_folder_path, exist_ok=True)

# Loop through all the zip files in the specified folder
for zip_filename in os.listdir(zip_folder_path):
    if zip_filename.endswith(".zip"):
        zip_file_path = os.path.join(zip_folder_path, zip_filename)
        try:
            # Open the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract all the contents into the extract folder
                zip_ref.extractall(extract_folder_path)
                print(f"Extracted: {zip_filename}")
        except Exception as e:
            print(f"Error extracting {zip_filename}: {e}")
