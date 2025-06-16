#Color picker/finder app

#Made by th3darkgem
#Discord - th3darkgem
#Made in 2025 June 16th
#If you want to use this for whatever reason, in your own project of any type, text me on discord


import tkinter as tk
import time
import pyperclip as clip
import pyautogui

root = tk.Tk()

# Define window
root.title("Color finder")
root.configure(background="darkgray")
root.geometry("450x300+50+50")
root.resizable(False, False)

# Window text
tk.Label(root, padx=10, pady=10, text="Click 'find' to find the color", bg="darkgray", fg="white", width=100, font=25).pack()
tk.Label(root, padx=10, text="Click the button and hover above the color with your mouse", bg="darkgray", fg="white", width=100, font=25).pack()
tk.Label(root, padx=10, pady=10, text="The color will be picked 3 seconds afer pressing the button", bg="darkgray", fg="white", width=100, font=25).pack()

# Find pixel color and turn it into hex
def found_color():
    time.sleep(3)
    posx, posy = pyautogui.position()
    r, g, b = pyautogui.pixel(posx, posy)
    global hex
    hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    root.config(bg=hex)

# Copy to clipboard
def addToClipBoard():
    clip.copy(hex)

# Picker button
find_color = tk.Button(root, width=100, command=found_color, activebackground="gray", text="Find color")
find_color.pack()

# Copy to clipboard button
copy_rgb = tk.Button(root, width=100, command=addToClipBoard, activebackground="gray", text="Copy to clipboard")
copy_rgb.pack()

# Color text
tk.Label(root, padx=10, pady=10, text="This is your picked color", bg="darkgray", fg="white", width=100, font=25).pack()

root.mainloop()