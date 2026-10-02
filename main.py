# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import os
import shutil
from pathlib import Path

EXTENSIONS = {
    "jpg": "image",
    "jpeg": "image",
    "png": "image",
    "webp": "image",
    "mp3": "audio",
    "wav": "audio",
    "pdf": "pdf",
}

def identifyFileType(file_name: str) -> str:
    return file_name.split(".")[-1].lower()

def moveToFolder(
    file: str,
    extension: str,
    input_dir: Path,
    output_dir: Path,
    dry_run: bool = False,
) -> None:
    source = input_dir / file
    subfolder = EXTENSIONS.get(extension, extension)
    target_dir = output_dir / subfolder

    dest_file = target_dir / file

    if dest_file.exists():
        stem: str = Path(file).stem
        ext_suffix: str = Path(file).suffix
        counter: int = 1
        while dest_file.exists():
            dest_file = target_dir / f"{stem}_{counter}{ext_suffix}"
            counter += 1

    if dry_run:
        print(f"[DRY-RUN] {source} -> {dest_file}")
        return

    target_dir.mkdir(parents=True, exist_ok=True)
    _ = shutil.move(str(source), str(dest_file))
    print(f"Moved: {source} -> {dest_file}")

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort files into category folders.")
    _ = parser.add_argument("-s", "--src", type=Path, default=Path("input"), help="Source directory")
    _ = parser.add_argument("-d", "--dest", type=Path, default=Path("output"), help="Destination directory")
    _ = parser.add_argument("--dry-run", action="store_true", help="Simulate without moving files")
    
    args: argparse.Namespace = parser.parse_args()

    src_dir: Path = Path(args.src)
    dest_dir: Path = Path(args.dest)
    dry_run: bool = bool(args.dry_run)

    src_dir.mkdir(exist_ok=True)
    if not dry_run:
        dest_dir.mkdir(exist_ok=True)

    files: list[str] = [
        str(f) for f in os.listdir(src_dir)
        if (src_dir / str(f)).is_file() and not str(f).startswith(".")
    ]

    for f in files:
        ext: str = identifyFileType(f)
        moveToFolder(f, ext, src_dir, dest_dir, dry_run=dry_run)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
