import os
import importlib
import subprocess

def get_python_files_in_directory(directory):
    python_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            python_files.append(filename)
    return python_files

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    python_files = get_python_files_in_directory(current_directory)

    if not python_files:
        print("No Python files found in the current directory.")
        return

    while True:
        print("Python files in the current directory:")
        for index, filename in enumerate(python_files, start=1):
            print(f"{index}. {filename}")

        selection = input("Enter the number of the Python file to run, or press Ctrl+C to exit: ")
        
        try:
            selection_index = int(selection) - 1
            selected_file = python_files[selection_index]

            module_name = selected_file[:-3]  # Remove the '.py' extension

            process = subprocess.Popen(["python3", module_name + ".py"], cwd=current_directory)
            process.wait()

            print(f"{module_name} execution finished.")
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nTerminating current process.")

if __name__ == "__main__":
    main()
