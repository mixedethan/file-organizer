# CLI File Organizer

# Brought into Existence by Ethan Wilson

**Version 1.0**

A Python CLI tool to organize files in a specified directory by categorizing them into folders based on their file extensions. This tool allows an easy way to declutter directories like your Downloads folder.

---

## Features
- Organizes files into predefined categories:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`
  - **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.pages`
  - **Videos**: `.mp4`, `.mkv`, `.mov`, `.avi`
  - **Music**: `.mp3`, `.wav`, `.aac`
  - **Archives**: `.zip`, `.tar`, `.rar`, `.gz`
  - **Others**: For uncategorized/unrecognized file types
- Creates folders for each category and moves files accordingly.
- Command-line interface (CLI) with support for macOS and future Windows functionality.

---

## Requirements
To use this project, ensure you have:
- Python 3.6 or later installed

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mixedethan/file_organizer.git
   cd file_organizer

2. Install dependencies:
    pip install -r requirements.txt

3. Run the script:
    python file-organizer.py <folder_path> [--os M|W]

## Usage
```bash
python file-organizer.py <folder_path> [--os M|W]
```
- Replace `<folder_path>` with the folder path which you'd like to organize.

### Specify Operating System (Work in Progess)
- Use the `--os` flag to specify Mac or Windowds (default: Mac):
  ```bash
  python file-organizer.py <folder_path> --os M
  ```

### Example Commands
```bash
python file-organizer.py /Users/ethanwilson/Downloads/ --os M
```

---

## Output
Example output for `python file-organizer.py /Users/ethanwilson/Downloads/ --os M`:
```
(base) ethanwilson@Ethans-MacBook-Air-5 file-organizer % python file-organizer.py /Users/ethanwilson/Downloads/ --os M
Found 3 files to organize in /Users/ethanwilson/Downloads/.
Moved: .DS_Store -> Others
Moved: DS_Store -> Others
Moved: Migos Trade Bars In 'Culture 3' Stamped Freestyle With The L.A. Leakers - Freestyle #111.mp3 -> Music
File organization is completed!
```

---

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

---

## Thank you for reading