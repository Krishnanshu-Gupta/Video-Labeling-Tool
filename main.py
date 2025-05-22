import os
import re

def get_run_number(filename):
    # Extract the run number from the filename
    match = re.search(r'Run(\d+)', filename)
    if match:
        return int(match.group(1))
    return 0

def rename_files():
    # Get the directory path
    directory = "After_May"

    # Pattern to match the prefix we want to remove (MATLAB and time)
    pattern = r"MATLAB \d{1,2}-\d{2} [AP]M "

    # List to store all filename pairs (new and original)
    filename_pairs = []

    # Get all files in the directory
    for filename in os.listdir(directory):
        print(filename)
        if filename.endswith('.csv'):
            # Create the new filename by removing the MATLAB and time prefix
            new_filename = re.sub(pattern, '', filename)
            filename_pairs.append((new_filename, filename))

            # Only rename if the new filename is different
            if new_filename != filename:
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)

                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"Error renaming {filename}: {str(e)}")

    # Sort the filename pairs by new filename (using the same sorting logic)
    filename_pairs.sort(key=lambda x: (x[0].split(',')[0], x[0].split(',')[1], get_run_number(x[0])))

    # Write sorted filename pairs to the text file
    with open('new_filenames.txt', 'w') as f:
        for new_filename, original_filename in filename_pairs:
            f.write(f"{new_filename}|{original_filename}\n")

if __name__ == "__main__":
    rename_files()
