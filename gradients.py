import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageDraw
import re


sizes = {
    "A4": (210, 297),
    "A5": (148, 210),
    "A6": (105, 148)
}

def create_gradient_image(width, height, color1, color2):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    for y in range(height):
        r = int(color1[0] * (height - y) / height + color2[0] * y / height)
        g = int(color1[1] * (height - y) / height + color2[1] * y / height)
        b = int(color1[2] * (height - y) / height + color2[2] * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return image

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def save_image(image, format_type):
    image_file = filedialog.asksaveasfilename(defaultextension="." + format_type.lower(),
                                               filetypes=[(format_type.upper(), "*." + format_type.lower())])
    if image_file:
        image.save(image_file)

def create_and_save_image():
    size_name = size_combobox.get().split()[0]
    width, height = sizes.get(size_name, (None, None))
    if width is None or height is None:
        print("Invalid size format")
        return
    
    color1 = hex_to_rgb(color1_entry.get())
    color2 = hex_to_rgb(color2_entry.get())
    format_type = format_combobox.get()

    gradient_image = create_gradient_image(width, height, color1, color2)
    save_image(gradient_image, format_type)

root = tk.Tk()
root.title("Gradient Image Creator")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0)

size_label = ttk.Label(main_frame, text="Image Size:")
size_label.grid(row=0, column=0, sticky="w")
size_combobox = ttk.Combobox(main_frame, values=["A4 (210x297)", "A5 (148x210)", "A6 (105x148)"], width=15)
size_combobox.current(0)
size_combobox.grid(row=0, column=1)

color1_label = ttk.Label(main_frame, text="Color 1 (Hex):")
color1_label.grid(row=1, column=0, sticky="w")
color1_entry = ttk.Entry(main_frame, width=20)
color1_entry.grid(row=1, column=1)

color2_label = ttk.Label(main_frame, text="Color 2 (Hex):")
color2_label.grid(row=2, column=0, sticky="w")
color2_entry = ttk.Entry(main_frame, width=20)
color2_entry.grid(row=2, column=1)

format_label = ttk.Label(main_frame, text="Save Format:")
format_label.grid(row=3, column=0, sticky="w")
format_combobox = ttk.Combobox(main_frame, values=["PNG", "JPEG", "BMP", "GIF"], width=10)
format_combobox.current(0)
format_combobox.grid(row=3, column=1)

create_button = ttk.Button(main_frame, text="Create & Save Image", command=create_and_save_image)
create_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
