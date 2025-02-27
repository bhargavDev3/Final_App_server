import iis_bridge.pool as pool
import subprocess
import ctypes
import sys
from app_main import client_name, date, app_pool_name

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def configure_app_pool():
    if not pool.exists(app_pool_name):
        pool.create(app_pool_name)
        print(f"Application Pool {app_pool_name} created successfully.")
    else:
        print(f"Application Pool {app_pool_name} already exists.")
    try:
        pool.config(app_pool_name, thirty_two_bit=True)
        pool.config(app_pool_name, idle_timeout="24:00:00")
        pool.config(app_pool_name, recycle_after_time="00:00:00")
        pool.config(app_pool_name, recycle_at_time="02:00:00")
        print(f"Application Pool {app_pool_name} configured successfully.")
    except Exception as e:
        print(f"An error occurred while configuring the application pool: {e}")

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    configure_app_pool()