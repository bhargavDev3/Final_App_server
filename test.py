import re
import os

# Define the client name and site
client_name = "Hallmark"  # This can be in any case (e.g., "hallmark", "HALLMARK", "Hallmark")
client_site = f"https://{client_name}.nimbleproperty.net"

# Function to find the correct case of the client_name in the path
def find_correct_case_path(base_path, client_name):
    # Get the list of directories in the base path
    if os.path.exists(base_path):
        for dir_name in os.listdir(base_path):
            # Compare case-insensitively
            if dir_name.lower() == client_name.lower():
                return os.path.join(base_path, dir_name)
    raise FileNotFoundError(f"Directory for client '{client_name}' not found in '{base_path}'")

# Define the base paths
base_path = r"C:\Production2"

# Find the correct case of the client_name in the base path
client_path = find_correct_case_path(base_path, client_name)

# Define the paths to the OCR files using the correct case of client_name
OCR_management = os.path.join(client_path, "Build", "OCR", "OCRManagement.js")
OCR_mapping = os.path.join(client_path, "Build", "OCR", "OCRFiles", "Scripts", "Mapping.js")

# Step 1: Replace the apiurl with the client_site (regardless of the current value)
def replace_apiurl(content):
    pattern = r"var apiurl = '[^']*';"
    replacement = f"var apiurl = '{client_site}/OCRWEBAPI/api';"
    return re.sub(pattern, replacement, content)

# Step 2: Replace the host with the client_site (regardless of the current value)
def replace_host(content):
    pattern = r"var host = '[^']*';"
    replacement = f"var host = '{client_site}';"
    return re.sub(pattern, replacement, content)

# Function to process a file
def process_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Perform the replacements
    content = replace_apiurl(content)
    content = replace_host(content)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"File '{file_path}' has been updated successfully.")

# Process both files
process_file(OCR_management)
process_file(OCR_mapping)