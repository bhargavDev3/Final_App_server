import re
import os
from app_main import client_name, base_path

def find_correct_case_path(base_path, client_name):
    if os.path.exists(base_path):
        for dir_name in os.listdir(base_path):
            if dir_name.lower() == client_name.lower():
                return os.path.join(base_path, dir_name)
    raise FileNotFoundError(f"Directory for client '{client_name}' not found in '{base_path}'")

client_path = find_correct_case_path(base_path, client_name)
dashboard_new_path = os.path.join(client_path, "Build", "Dashboard_New", "js", "dashboard_New.js")
dashboard_new_chart_path = os.path.join(client_path, "Build", "Dashboard_New", "js", "Dashboard_NewCharts.js")

def modify_file_content(file_path, client_name):
    with open(file_path, 'r') as file:
        content = file.read()
    content = re.sub(r'var api_server_ip = "https://[^"]+";', 
                     r'var api_server_ip = "https://dashboardapi.nimbleproperty.net";', 
                     content)
    content = re.sub(r'var client = "[^"]+";', 
                     f'var client = "{client_name}";', 
                     content)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' has been updated successfully.")

modify_file_content(dashboard_new_path, client_name)
modify_file_content(dashboard_new_chart_path, client_name)