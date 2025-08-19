import sys
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_files():
    filenames = filedialog.askopenfilenames(
        title="Select media files (optional)",
        filetypes=(
            ("Media files", "*.jpg *.jpeg *.png *.mp4 *.mov *.avi *.mkv"),
            ("All files", "*.*")
        )
    )
    if filenames:
        media_entry.delete(0, tk.END)
        media_entry.insert(0, ";".join(filenames))

def run_script():
    contact = contact_entry.get().strip()
    caption = caption_entry.get().strip()
    media_paths = media_entry.get().strip()

    if not contact or not caption:
        messagebox.showerror("Missing Fields", "Contact and Caption are required!")
        return

    # Build command for whatsapp.py
    cmd = [sys.executable, os.path.join(os.getcwd(), "whatsapp.py"), contact, caption]
    if media_paths:
        cmd.append(media_paths)

    try:
        # Run whatsapp.py
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", f"Message sent to '{contact}' successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running whatsapp.py:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")

# ---- GUI Setup ----
root = tk.Tk()
root.title("WhatsApp Auto Sender")
root.geometry("720x260")

tk.Label(root, text="Contact Name / Group:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
contact_entry = tk.Entry(root, width=72)
contact_entry.grid(row=0, column=1, pady=6, padx=6)

tk.Label(root, text="Caption:").grid(row=1, column=0, sticky="e", padx=6, pady=6)
caption_entry = tk.Entry(root, width=72)
caption_entry.grid(row=1, column=1, pady=6, padx=6)

tk.Label(root, text="Media Files (optional):").grid(row=2, column=0, sticky="e", padx=6, pady=6)
media_entry = tk.Entry(root, width=72)
media_entry.grid(row=2, column=1, pady=6, padx=6)
tk.Button(root, text="Browse", command=browse_files).grid(row=2, column=2, padx=6, pady=6)

tk.Button(root, text="Send via WhatsApp", command=run_script, bg="#25D366", fg="white", width=20).grid(row=4, column=1, pady=14)

root.mainloop()
