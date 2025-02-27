import re

# Define the client name
client_name = "pink"

# Define the paths to the files
dashboard_new_path = r"C:\Production2\Hallmark\Build\Dashboard_New\js\dashboard_New.js"
dashboard_new_chart_path = r"C:\Production2\Hallmark\Build\Dashboard_New\js\Dashboard_NewCharts.js"

# Function to modify the file content
def modify_file_content(file_path, client_name):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Step 1: Remove "staging" from the api_server_ip variable
    content = re.sub(r'var api_server_ip = "https://stagingdashboardapi\.nimbleproperty\.net";', 
                     r'var api_server_ip = "https://dashboardapi.nimbleproperty.net";', 
                     content)

    # Step 2: Replace "STAGING1" with the client name
    content = re.sub(r'var client = "STAGING1";', 
                     f'var client = "{client_name}";', 
                     content)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"File '{file_path}' has been updated successfully.")

# Modify both files
modify_file_content(dashboard_new_path, client_name)
modify_file_content(dashboard_new_chart_path, client_name)