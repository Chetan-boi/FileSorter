# 📁 FileSorter

A lightweight and efficient Python script designed to clean up and organize your directories automatically. It monitors or scans an `input` directory and categorizes files into clean, dedicated subdirectories inside `output` based on their file extensions.

---

## ✨ Features

- **Automated Categorization:** Dynamically reads files and moves them to matching extension folders (e.g., `.pdf` goes to `output/pdf/`).
- **Specialized Rules:** Custom mappings for specific types (e.g., `.jpg` and `.jpeg` are grouped together under `output/image/`).
- **Safety Filtering:** Automatically ignores hidden system files (like `.DS_Store` or `.gitkeep`).
- **Simple & Zero-Dependency:** Uses built-in Python modules (`os`, `shutil`, `pathlib`).

---

## 📂 Project Structure

```text
FileSorter/
├── input/               # Drop your unorganized files here
│   └── .gitkeep
├── output/              # Categorized folders are generated here
│   ├── image/           # Target folder for jpg, jpeg
│   ├── pdf/             # Target folder for pdf
│   └── .gitkeep
├── main.py              # Main execution script
├── .gitignore           # Git ignore configurations (ignores input/output contents)
└── README.md            # Project documentation (this file)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation & Run

1. Clone or download this repository.
2. Put any files you want to organize into the `input/` directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Find your organized files structured cleanly in the `output/` directory!

---

## 🔧 Customizing Mappings

You can customize how files are grouped by editing the `moveToFolder` function in [main.py](file:///Users/chetan/Desktop/FileSorter/main.py). 

For example, to group all audio files (`.mp3`, `.wav`) into an `audio` folder:

```python
def moveToFolder(file, extension):
    source = "input/" + file
    if extension in ["jpeg", "jpg"]:
        destination = "output/image/"
    elif extension in ["mp3", "wav"]:
        destination = "output/audio/"
    else:
        destination = "output/" + extension + "/"

    shutil.move(source, destination)
```
