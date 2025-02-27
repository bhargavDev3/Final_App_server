import re
import os
from app_main import client_name, base_path

client_site = f"https://{client_name}.nimbleproperty.net"

def find_correct_case_path(base_path, client_name):
    if os.path.exists(base_path):
        for dir_name in os.listdir(base_path):
            if dir_name.lower() == client_name.lower():
                return os.path.join(base_path, dir_name)
    raise FileNotFoundError(f"Directory for client '{client_name}' not found in '{base_path}'")

client_path = find_correct_case_path(base_path, client_name)
OCR_management = os.path.join(client_path, "Build", "OCR", "OCRManagement.js")
OCR_mapping = os.path.join(client_path, "Build", "OCR", "OCRFiles", "Scripts", "Mapping.js")

def replace_apiurl(content):
    pattern = r"var apiurl = '[^']*';"
    replacement = f"var apiurl = '{client_site}/OCRWEBAPI/api';"
    return re.sub(pattern, replacement, content)

def replace_host(content):
    pattern = r"var host = '[^']*';"
    replacement = f"var host = '{client_site}';"
    return re.sub(pattern, replacement, content)

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = replace_apiurl(content)
    content = replace_host(content)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' has been updated successfully.")

process_file(OCR_management)
process_file(OCR_mapping)