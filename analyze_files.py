import os

try:
    from .build_directory_md import get_good_file_paths
except ImportError:
    from build_directory_md import get_good_file_paths  # type: ignore

def analyze_files(file_paths):
    uppercase_files = [file for file in file_paths if file != file.lower()]
    space_files = [file for file in file_paths if " " in file]
    hyphen_files = [file for file in file_paths if "-" in file]
    no_directory_files = [file for file in file_paths if os.sep not in file]

    return uppercase_files, space_files, hyphen_files, no_directory_files

def print_results(category_name, files):
    if files:
        print(f"{len(files)} files contain {category_name}:")
        print("\n".join(files) + "\n")

if __name__ == "__main__":
    try:
        file_paths = list(get_good_file_paths())
        assert file_paths, "get_good_file_paths() failed!"

        uppercase_files, space_files, hyphen_files, no_directory_files = analyze_files(file_paths)

        print_results("uppercase characters", uppercase_files)
        print_results("space characters", space_files)
        print_results("hyphen characters", hyphen_files)
        print_results("no directory", no_directory_files)

        total_bad_files = len(uppercase_files) + len(space_files) + len(hyphen_files) + len(no_directory_files)
        if total_bad_files:
            import sys
            sys.exit(total_bad_files)

    except Exception as e:
        print(f"An error occurred: {e}")
