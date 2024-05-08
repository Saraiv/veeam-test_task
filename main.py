import os
import shutil
import sys
import time
import argparse

# Synchronize the contents of a source folder with a replica folder.
def synchronize_folders(source_folder, replica_folder, log_file=None):
    if not os.path.exists(source_folder) or not os.path.exists(replica_folder):
        return
    
    source_files = set()

    # Collect source and replica files
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        replica_root = os.path.join(replica_folder, relative_path)

        os.makedirs(replica_root, exist_ok=True)
        
        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)

            source_files.add(os.path.normpath(replica_file))  # Add replica file to set

            if not os.path.exists(replica_file) or os.path.getmtime(source_file) != os.path.getmtime(replica_file):
                shutil.copy2(source_file, replica_file)
                # Log the action
                print(f"Copied '{source_file}' to '{replica_file}'")
            else:
                # Log the action
                print(f"File '{source_file}' is up-to-date")

    # Remove files that are not in the source folder
    for root, dirs, files in os.walk(replica_folder):
        for file in files:
            replica_file = os.path.join(root, file)

            # Log the action
            if replica_file not in source_files:
                os.remove(replica_file)
                print(f"Removed '{replica_file}' as it does not exist in source folder")

# Synchronization should be performed periodically the given interval in seconds.
def sync_periodically(source_folder, replica_folder, interval):
    while True:
        synchronize_folders(source_folder, replica_folder)
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description='Synchronize the contents of a source folder with a replica folder.')
    parser.add_argument('source_folder', type=str, help='The source folder to synchronize.')
    parser.add_argument('replica_folder', type=str, help='The replica folder to synchronize.')
    parser.add_argument('--interval', type=int, default=3600, help='The interval in seconds to perform synchronization periodically.')
    parser.add_argument('--log_file', type=str, help='Path to the log file.')
    args = parser.parse_args()

    # Set log file if provided
    if args.log_file:
        sys.stdout = open(args.log_file, "w")

    sync_periodically(args.source_folder, args.replica_folder, args.interval)

    return 0

if __name__ == "__main__":
    main()