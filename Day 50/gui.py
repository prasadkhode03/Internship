import sys
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_files():
    filenames = filedialog.askopenfilenames(
        title="Select media files",
        filetypes=(
            ("Media files", "*.jpg *.jpeg *.png *.mp4 *.mov *.avi *.mkv"),
            ("All files", "*.*")
        )
    )
    if filenames:
        media_entry.delete(0, tk.END)
        media_entry.insert(0, ";".join(filenames))
    # filedialog closes automatically after selection

def run_script():
    title = title_entry.get().strip()
    text = text_entry.get().strip()
    hashtags = hashtags_entry.get().strip()
    media_paths = media_entry.get().strip()
    option = option_var.get().strip()

    if not title or not text or not option:
        messagebox.showerror("Missing Fields", "Title, Text, and Option are required!")
        return

    # Use the same Python interpreter to run linkedin.py
    cmd = [sys.executable, os.path.join(os.getcwd(), "linkedin.py"), title, text, hashtags, media_paths, option]
    try:
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", f"Post for '{option}' completed (check LinkedIn).")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running linkedin.py:\n{e}")

root = tk.Tk()
root.title("LinkedIn Auto Poster")
root.geometry("700x300")

tk.Label(root, text="Title:").grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(root, width=70)
title_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Text:").grid(row=1, column=0, sticky="e")
text_entry = tk.Entry(root, width=70)
text_entry.grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Hashtags:").grid(row=2, column=0, sticky="e")
hashtags_entry = tk.Entry(root, width=70)
hashtags_entry.grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Media Files:").grid(row=3, column=0, sticky="e")
media_entry = tk.Entry(root, width=70)
media_entry.grid(row=3, column=1, pady=5, padx=5)
tk.Button(root, text="Browse", command=browse_files).grid(row=3, column=2, padx=5)

tk.Label(root, text="Post Option:").grid(row=4, column=0, sticky="e")
option_var = tk.StringVar(value="Only Article")
tk.OptionMenu(root, option_var, "Only Article", "Video Only", "Image Posts").grid(row=4, column=1, sticky="w")

tk.Button(root, text="Post to LinkedIn", command=run_script, bg="green", fg="white").grid(row=5, column=1, pady=15)

root.mainloop()
