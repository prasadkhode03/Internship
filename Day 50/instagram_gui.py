# gui_instagram.py
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

def run_script():
    caption = caption_entry.get().strip()
    media_paths = media_entry.get().strip()

    if not caption or not media_paths:
        messagebox.showerror("Missing Fields", "Caption and Media files are required!")
        return

    # Run instagram.py with same Python interpreter
    cmd = [sys.executable, os.path.join(os.getcwd(), "instagram.py"), caption, media_paths]
    try:
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", "Instagram post completed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running instagram.py:\n{e}")

root = tk.Tk()
root.title("Instagram Auto Poster")
root.geometry("700x250")

tk.Label(root, text="Caption:").grid(row=0, column=0, sticky="e")
caption_entry = tk.Entry(root, width=70)
caption_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Media Files:").grid(row=1, column=0, sticky="e")
media_entry = tk.Entry(root, width=70)
media_entry.grid(row=1, column=1, pady=5, padx=5)
tk.Button(root, text="Browse", command=browse_files).grid(row=1, column=2, padx=5)

tk.Button(root, text="Post to Instagram", command=run_script, bg="purple", fg="white").grid(row=3, column=1, pady=15)

root.mainloop()