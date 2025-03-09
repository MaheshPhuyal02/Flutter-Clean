import os
import subprocess

def run_flutter_clean(directory):
    # Change to the project directory
    os.chdir(directory)
    # Run the flutter clean command
    result = subprocess.run(["flutter", "clean"], capture_output=True, text=True)
    # Print the output of the flutter clean command
    print(f"Running 'flutter clean' in {directory}")
    print(result.stdout)
    print(result.stderr)

def traverse_and_clean(root_directory):
    # Traverse through the root directory
    for root, dirs, files in os.walk(root_directory):
        for dir_name in dirs:
            project_path = os.path.join(root, dir_name)
            # Check if the directory contains a Flutter project by looking for pubspec.yaml
            if "pubspec.yaml" in os.listdir(project_path):
                run_flutter_clean(project_path)
        # Prevent os.walk from going into subdirectories
        break

if __name__ == "__main__":
    root_dir = os.getcwd()  # Set the root directory to the current directory of the terminal
    traverse_and_clean(root_dir)
