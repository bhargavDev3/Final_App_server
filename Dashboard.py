import re
import os

# Define the client name
client_name = "hallmark"  # This can be in any case (e.g., "pink", "Pink", "PINK")

# Function to find the correct case of the client_name in the path
def find_correct_case_path(base_path, client_name):
    # Get the list of directories in the base path
    if os.path.exists(base_path):
        for dir_name in os.listdir(base_path):
            # Compare case-insensitively
            if dir_name.lower() == client_name.lower():
                return os.path.join(base_path, dir_name)
    raise FileNotFoundError(f"Directory for client '{client_name}' not found in '{base_path}'")

# Define the base path
base_path = r"C:\Production2"

# Find the correct case of the client_name in the base path
client_path = find_correct_case_path(base_path, client_name)

# Define the paths to the files using the correct case of client_name
dashboard_new_path = os.path.join(client_path, "Build", "Dashboard_New", "js", "dashboard_New.js")
dashboard_new_chart_path = os.path.join(client_path, "Build", "Dashboard_New", "js", "Dashboard_NewCharts.js")

# Function to modify the file content
def modify_file_content(file_path, client_name):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Step 1: Replace any api_server_ip value with the desired one
    content = re.sub(r'var api_server_ip = "https://[^"]+";', 
                     r'var api_server_ip = "https://dashboardapi.nimbleproperty.net";', 
                     content)

    # Step 2: Replace any client value with the provided client_name
    content = re.sub(r'var client = "[^"]+";', 
                     f'var client = "{client_name}";', 
                     content)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"File '{file_path}' has been updated successfully.")

# Modify both files
modify_file_content(dashboard_new_path, client_name)
modify_file_content(dashboard_new_chart_path, client_name)