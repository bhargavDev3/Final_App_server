import subprocess
import ctypes
import sys

client_name = "Hallmark"
site_name = client_name 
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def stop_iis_site(site_name):
    try:
        subprocess.run(["powershell", "-Command", f"Stop-Website -Name '{site_name}'"], check=True)
        print(f"Site '{site_name}' stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop the site: {e.stderr}")

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    stop_iis_site(site_name)  # Replace with your site name