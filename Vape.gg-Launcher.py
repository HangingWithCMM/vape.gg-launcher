from tkinter import *
from PIL import ImageTk, Image
import os
import json
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry("370x80")
root.title("Vape.gg Launcher")
root.configure(bg="#2c2f33")
root.iconbitmap('Assets/Fav.ico')

DEFAULT_VAPE_V4_PATH = "path_to_vape_v4_exe"
DEFAULT_VAPE_LITE_PATH = "path_to_vape_lite_exe"

VAPES_PATHS_FILE = "Assets/vape_paths.json"

try:
    with open(VAPES_PATHS_FILE, 'r') as f:
        vape_paths = json.load(f)
except FileNotFoundError:
    vape_paths = {
        "vape_v4_path": DEFAULT_VAPE_V4_PATH,
        "vape_lite_path": DEFAULT_VAPE_LITE_PATH
    }

def save_vape_paths():
    with open(VAPES_PATHS_FILE, 'w') as f:
        json.dump(vape_paths, f)

def launch_vape_v4():
    os.startfile(vape_paths["vape_v4_path"])

def launch_vape_lite():
    os.startfile(vape_paths["vape_lite_path"])

def download_vape():
    os.startfile("https://www.vape.gg/download")

def browse_vape_v4_exe(event):
    filename = askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if filename:
        vape_paths["vape_v4_path"] = filename
        save_vape_paths()

def browse_vape_lite_exe(event):
    filename = askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if filename:
        vape_paths["vape_lite_path"] = filename
        save_vape_paths()

vape_v4_image = Image.open("Assets/VAPE-V4.png")
vape_v4_image.thumbnail((100, 100), Image.LANCZOS)
vape_v4_image = ImageTk.PhotoImage(vape_v4_image)

vape_lite_image = Image.open("Assets/VAPE-LITE.png")
vape_lite_image.thumbnail((100, 100), Image.LANCZOS)
vape_lite_image = ImageTk.PhotoImage(vape_lite_image)

vape_v4_button = Button(root, text="Launch Vape V4", command=launch_vape_v4, image=vape_v4_image, bg="#7289da", fg="white", activebackground="#677bc4", activeforeground="white")
vape_v4_button.image = vape_v4_image
vape_v4_button.pack(pady=10, padx=5, side=LEFT)
vape_v4_button.bind("<Button-3>", browse_vape_v4_exe)

download_vape_label = Label(root, text="Download Vape", fg="#7289da", cursor="hand2")
download_vape_label.pack(pady=5, side=LEFT)
download_vape_label.bind("<Button-1>", lambda e: download_vape())
download_vape_label.configure(bg="#2c2f33")

vape_lite_button = Button(root, text="Launch Vape Lite", command=launch_vape_lite, image=vape_lite_image, bg="#7289da", fg="white", activebackground="#677bc4", activeforeground="white")
vape_lite_button.image = vape_lite_image
vape_lite_button.pack(pady=10, padx=5, side=LEFT)
vape_lite_button.bind("<Button-3>", browse_vape_lite_exe)

vape_v4_button.pack(side=LEFT, expand=True, fill=BOTH, anchor=CENTER)
download_vape_label.pack(side=LEFT, expand=True, fill=BOTH, anchor=CENTER)
vape_lite_button.pack(side=LEFT, expand=True, fill=BOTH, anchor=CENTER)

root.pack_propagate(False)
root.mainloop()
