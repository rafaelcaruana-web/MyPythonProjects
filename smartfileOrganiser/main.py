from pathlib import Path
import shutil
from datetime import datetime


import tkinter as tk
from tkinter import filedialog


def checkfile(extension):
    if extension in [".jpg",".jpeg",".png",".gif",".webp"]:
        return("Images")
    elif extension in [".pdf",".txt",".docx",".doc",".pptx",".xlsx"]:
        return("Documents")
    elif extension in [".mp4",".mov",".avi",".mkv"]:
        return("Videos")
    else:
        return("Other")

selected_folder = ""
root = tk.Tk()

root.title("Smart File Organiser")
root.geometry("700x500")
root.configure(bg="#151922")

def organise_files():
    if not selected_folder:
        print("Please select a folder first.")
        return

    folder = Path(selected_folder)

    folder_names = ["Images", "Documents", "Videos", "Other"]

    # Create the destination folders
    for name in folder_names:
        (folder / name).mkdir(exist_ok=True)

    # Counters for the report
    file_counts = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Other": 0
    }

    skipped_count = 0

    # Organise files
    for item in folder.iterdir():
        if item.is_file():
            filetype = checkfile(item.suffix)
            destination = folder / filetype
            destination_file = destination / item.name

            if destination_file.exists():
                print("Skipped:", item.name)
                skipped_count += 1
            else:
                shutil.move(item, destination)
                file_counts[filetype] += 1
                print("Moved:", item.name, "->", filetype)

    total_moved = sum(file_counts.values())

    results_label.config(
        text=(
            f"Organisation complete!\n\n"
            f"Images moved: {file_counts['Images']}\n"
            f"Documents moved: {file_counts['Documents']}\n"
            f"Videos moved: {file_counts['Videos']}\n"
            f"Other moved: {file_counts['Other']}\n\n"
            f"Total moved: {total_moved}\n"
            f"Files skipped: {skipped_count}"
        )
    )


def browse_folder():
    global selected_folder
    selected = filedialog.askdirectory()

    if selected:
        selected_folder = selected
        folder_label.config(text=selected)

title_label = tk.Label(
    root,
    text="Smart File Organiser",
    font=("Helvetica", 24, "bold"),
    bg="#151922",
    fg="#5EEAD4"
)

title_label.pack(pady=(35, 10))

subtitle_label = tk.Label(
    root,
    text="Keep your files organised, automatically.",
    font=("Helvetica", 11),
    bg="#151922",
    fg="#AAB5C5"
)

subtitle_label.pack(pady=(10, 10))

folder_label = tk.Label(
    root,
    text="No folder selected",
    font=("Helvetica", 10),
    bg="#151922",
    fg="#AAB5C5",
    wraplength=600
)

folder_label.pack(pady=10)

results_label = tk.Label(
    root,
    text="Your results will appear here.",
    bg="#151922",
    fg="white",
    font=("Helvetica", 12),
    wraplength=600
)
results_label.pack(pady=10)

browse_button = tk.Button(
    root,
    text="Browse Folder",
    command=browse_folder,
    font=("Helvetica",12),
    bg="#5EEAD4",
    fg="#151922",
    padx=20,
    pady=10,
    cursor="hand2"
)

browse_button.pack(pady=25)

organise_button = tk.Button(
    root,
    text="Organise Files",
    command=organise_files,
    font=("Helvetica", 12, "bold"),
    bg="#5EEAD4",
    fg="#151922",
    padx=25,
    pady=12,
    cursor="hand2"
)

organise_button.pack(pady=10)

root.mainloop()
