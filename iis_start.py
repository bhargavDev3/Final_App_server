import subprocess
import ctypes
import sys

client_name = "Hallmark"
site_name = client_name  # Replace with your site name

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def start_iis_site(site_name):
    try:
        # Use PowerShell to start the IIS site
        subprocess.run(["powershell", "-Command", f"Start-Website -Name '{site_name}'"], check=True)
        print(f"Site '{site_name}' started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start the site: {e.stderr}")

if not is_admin():
    # Request admin privileges if not already running as admin
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    # Start the IIS site if running as admin
    start_iis_site(site_name)