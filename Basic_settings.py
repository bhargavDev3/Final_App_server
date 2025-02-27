import subprocess
import ctypes
import sys

# Define variables
client_name = "Hallmark"
date = "26022025"
app_pool_name = f"{client_name}_{date}"
site_name = client_name
application_name = "OCRWEBAPI"

# Function to check if the script is running as administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Function to run a command with elevated privileges
def run_elevated_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("Command output:", result.stdout)
        if result.stderr:
            print("Command error:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

# Function to change the application pool for the root application of the site
def change_root_app_pool(site_name, app_pool_name):
    command = f'%windir%\\system32\\inetsrv\\appcmd.exe set app /app.name:"{site_name}/" /applicationPool:"{app_pool_name}"'
    print(f"Changing application pool for root application of site '{site_name}' to '{app_pool_name}'...")
    if run_elevated_command(command):
        print(f"Successfully changed application pool for root application of site '{site_name}'.")
    else:
        print(f"Failed to change application pool for root application of site '{site_name}'.")

# Function to change the application pool for the application
def change_app_app_pool(site_name, application_name, app_pool_name):
    command = f'%windir%\\system32\\inetsrv\\appcmd.exe set app /app.name:"{site_name}/{application_name}" /applicationPool:"{app_pool_name}"'
    print(f"Changing application pool for application '{application_name}' to '{app_pool_name}'...")
    if run_elevated_command(command):
        print(f"Successfully changed application pool for application '{application_name}'.")
    else:
        print(f"Failed to change application pool for application '{application_name}'.")

# Main script
if __name__ == "__main__":
    # Check if the script is running as administrator
    if not is_admin():
        # Re-run the script with elevated privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        # Change the application pool for the root application of the site
        change_root_app_pool(site_name, app_pool_name)

        # Change the application pool for the application
        change_app_app_pool(site_name, application_name, app_pool_name)

        print("Process completed.")