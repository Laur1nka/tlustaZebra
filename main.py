import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Viewer")

heading = tk.Label(root, text="Tlustý Zebry !!!", font=("Arial", 16, "bold"))
heading.pack(pady=10)

img = Image.open("zebraImage.png")
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(root, image=photo)
img_label.pack(pady=10)

root.mainloop()