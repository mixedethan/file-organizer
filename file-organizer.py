import os
import shutil
import argparse



# TODO: Add functionality for Windows
# TODO: Possibly create an application rather than using a CLI

# usage:    python file-organizer.py /Users/ethanwilson/Downloads/ --os M

# define all the file categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".pages"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".rar", ".gz"],
    "Others": []  # for uncategorized/unrecognized file types
}


# parser to handle cl arguments
parser = argparse.ArgumentParser(description='A file organizer tool')

# folder to organize argument
parser.add_argument(
    'folder',
    type=str,          
    help='Enter the file path of the folder to be organized'
)

# argument flags for temperature units
parser.add_argument(
    '--os',
    choices=['M','W'],
    default='M',
    help="Select an OS: M for Mac OSX, W for Windows OS (Default is set to: M)."
)

args = parser.parse_args()

# retrieve folder path from user
folder_to_organize = args.folder

# check if category folder exists
if not os.path.exists(folder_to_organize):
    print("Invalid path. Please check the folder path and try again.")
    exit()

# list all files in the folder
entries = os.listdir(folder_to_organize)

# will store all file names within designated folder
files = []

# check for only files & not directories
for entry in entries:
    full_path = os.path.join(folder_to_organize, entry)
    # ex full_path = /Downloads/resume.pdf

    if os.path.isfile(full_path):
        files.append(entry)


print(f"Found {len(files)} files to organize in {folder_to_organize}.")

# place files into the category function
def categorize_file(filename):
    for category, extensions in CATEGORIES.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            return category
    return "Others"

# create the folders for each category
for category in CATEGORIES.keys():
    category_folder = os.path.join(folder_to_organize, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

# move the files into each folder
for file in files:
    category = categorize_file(file)
    source = os.path.join(folder_to_organize, file)
    destination = os.path.join(folder_to_organize, category, file)
    
    shutil.move(source, destination)
    print(f"Moved: {file} -> {category}")

print("File organization is completed!")
