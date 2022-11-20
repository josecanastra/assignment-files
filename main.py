__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Imports
import os
import time
import zipfile


def cache_path():
    main_dir_path = os.path.dirname(__file__) # Get the parent directory of the script file
    cache_dir_name = "cache"
    return os.path.join(main_dir_path, cache_dir_name)


### Part 1: Create or clean cache directory
def clean_cache():
    
    # Check if cache directory does not exist 
    if not os.path.exists(cache_path()):
        os.mkdir(cache_path()) # Create directory
        print("\nCache directory created!\n")

    # Check if cache directory exist and if directory is not empty
    elif os.path.exists(cache_path()) and os.listdir(cache_path()) != []:
        for file in os.listdir(cache_path()):
            os.remove(os.path.join(cache_path(), file)) # Clean up cache directory
        print("\nCached files deleted!\n")

    else:
        print("\nCache directory is already empty!\n")
### End Part 1


### Part 2: Extract the zip file
def cache_zip(zip_file: str, cache_dir_name: str):

    # Zip file path
    zip_file_path = os.path.join(os.path.dirname(__file__), zip_file)
    
    time.sleep(1)
    print(f"Extracting new files to: {cache_path()}")
    
    with zipfile.ZipFile(zip_file_path, "r") as zip:
        zip.extractall(cache_path()) # Extract zip to cache directory

    time.sleep(1)
    print("Extracting completed!\n")
### End Part 2


### Part 3: Create cached files list
def cached_files():

    # List cached files
    cached_files_list = []

    # Absolute path of the files in the cache directory
    for file in os.listdir(cache_path()):
        file_abs_path = os.path.join(cache_path(), file)
        cached_files_list.append(file_abs_path)

    return cached_files_list
### End Part 3


### Part 4: Find password
def find_password(list):
    
    time.sleep(1)
    print("Finding password...")
    
    # Open file using the path in the cached files list
    for path in list:
        file = open(path, "r")
        lines = file.readlines()

        # Search for the string password
        for word in lines:
            search_for = "password"
            if word.find(search_for) == 0:
                split = word.split()
                time.sleep(1)
                return split[1] # Return the password
### End Part 4


### This block is only executed if this script is run directly (main.py)
if __name__ == "__main__":
    clean_cache() # Part 1
    cache_zip("data.zip", "cache") # Part 2
    cached_files() # Part 3
    print(f"{find_password(cached_files())}\n") # Part 4