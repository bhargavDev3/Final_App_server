import os
import shutil
import time

# Define client name
client_name = "hallmark"

# Define paths
client_path = fr"C:/Production2/{client_name}/Build"
New_Build_Source = r"C:/Production_release/NewBuild_13022025/NewBuild"

def update_timestamp(path):
    """Update the last modified timestamp of a file or folder to the current time."""
    current_time = time.time()
    os.utime(path, (current_time, current_time))

def clean_directory(client_path):
    """Delete all folders and files in client_path except MailContent folder and Web.config file."""
    # Ensure the path exists
    if not os.path.exists(client_path):
        print(f"The path {client_path} does not exist.")
        return

    # Iterate over all items in the directory
    for item in os.listdir(client_path):
        item_path = os.path.join(client_path, item)
        
        # Skip the MailContent folder and Web.config file
        if item == "MailContent" or item == "Web.config":
            print(f"Skipping {item}")
            continue
        
        # Remove the item
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                print(f"Deleted file: {item}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item}")
        except Exception as e:
            print(f"Failed to delete {item}. Reason: {e}")

def copy_except_excluded(New_Build_Source, client_path):
    """Copy all folders and files from New_Build_Source to client_path except MailContent folder and Web.config file."""
    # Ensure both paths exist
    if not os.path.exists(New_Build_Source):
        print(f"Source path {New_Build_Source} does not exist.")
        return
    if not os.path.exists(client_path):
        print(f"Destination path {client_path} does not exist.")
        return

    # Iterate over all items in the source directory (New_Build_Source)
    for item in os.listdir(New_Build_Source):
        source_item_path = os.path.join(New_Build_Source, item)
        destination_item_path = os.path.join(client_path, item)

        # Skip the MailContent folder and Web.config file
        if item == "MailContent" or item == "Web.config":
            print(f"Skipping {item}")
            continue

        # Copy the item
        try:
            if os.path.isfile(source_item_path):
                shutil.copy2(source_item_path, destination_item_path)
                print(f"Copied file: {item}")
            elif os.path.isdir(source_item_path):
                shutil.copytree(source_item_path, destination_item_path)
                print(f"Copied folder: {item}")

            # Update the last modified timestamp to the current time
            update_timestamp(destination_item_path)
            print(f"Updated timestamp for: {item}")
        except Exception as e:
            print(f"Failed to copy {item}. Reason: {e}")

# Step 1: Clean client_path (delete all except MailContent and Web.config)
print("Step 1: Cleaning client_path...")
clean_directory(client_path)

# Step 2: Copy from New_Build_Source to client_path (except MailContent and Web.config)
print("\nStep 2: Copying from New_Build_Source to client_path...")
copy_except_excluded(New_Build_Source, client_path)

print("\nProcess completed!")