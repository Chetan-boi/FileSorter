# FileSorter

A Python utility to sort unorganized files from an input directory into categorized subdirectories based on file extensions.

---
## Features

- **Automated Categorization:** Dynamically reads files and moves them to matching extension folders (e.g., `.pdf` goes to `output/pdf/`).
- **CLI Options:** Supports custom source and destination directories via command-line arguments.
- **Dry-Run Mode:** Test and preview file moves without altering your disk.
- **Collision Handling:** Automatically appends an incrementing suffix (`_1`, `_2`) if a file with the same name already exists in the destination.
- **Safety Filtering:** Ignores hidden system files (like `.DS_Store` or `.gitkeep`).
- **Simple & Zero-Dependency:** Uses built-in Python standard library modules (`os`, `shutil`, `pathlib`, `argparse`).

---

## Getting Started

### Prerequisites
- Python 3.9+ installed on your system.

### Installation & Run

1. Clone or download this repository.
2. Put any files you want to organize into the `input/` directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Find your organized files structured cleanly in the `output/` directory!

---

### Command-Line arguments

| Flag | Long Flag | Description | Default |
| :--- | :--- | :--- | :--- |
| `-s` | `--src` | Source directory to scan | `input` |
| `-d` | `--dest` | Destination directory for sorted files | `output` |
|  | `--dry-run` | Preview file moves without modifying the disk | `False` |
| `-h` | `--help` | Show the help message and exit | | 


---

## Configuration

Modify `EXTENTIONS` in `main.py` to customize category destinations:

```python
EXTENTIONS = {
    "png": "image",
    "mp4": "video",
    "tar": "archives",
}
```
