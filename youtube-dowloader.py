from yt_dlp import YoutubeDL


import tkinter as tk
from tkinter import font 
from tkinter import filedialog

# GUI
root = tk.Tk()
root.title("youtube downloader")
root.geometry("500x500")


# Create a custom font for the heading
heading_font = font.Font(family="Helvetica", size=20, weight="bold")

# Create the heading label
heading_label = tk.Label(root, text="Enter your link in the box.", font=heading_font)
heading_label.pack(pady=20)

# The variable to hold the text from the entry
Link_var = tk.StringVar()

# Entry widget connected to the variable
text_entry = tk.Entry(root, textvariable=Link_var, font=("Helvetica", 14), width=30)
text_entry.pack(pady=10)

if Link_var.get() == "":
    text_entry.insert(0, "https://www.youtube.com/watch?v=P8vtPmJE1FY")  # Default text

# Function to print the text when a button is clicked
def Link_converter():
    print("You Link:", Link_var.get())
    print("Your format:", Format_var.get())
    print("Your destination:", destination_var.get())
    
    if Format_var.get() == "WEBM":
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': destination_var.get() + '/%(title)s.%(ext)s',
        }
        
    elif Format_var.get() == "MP4":
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': destination_var.get() + '/%(title)s.%(ext)s',
        }
        
    elif Format_var.get() == "original":
    
        ydl_opts = {
            'format': 'best',
            'outtmpl': destination_var.get() + '/%(title)s.%(ext)s',
        }
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([Link_var.get()])

# format heading
format_heading = tk.Label(root, text="Choose Your Type of file", font=heading_font)
format_heading.pack(pady=10)

# format variable and options
Format_var = tk.StringVar()
Format_var.set("MP4")  # default value
options = ["MP4", "WEBM", "original"]

# format menu widget
format = tk.OptionMenu(root, Format_var, *options)
format.config(font=("Helvetica", 12), width=20)
format.pack(pady=5)

# Destination heading
destination_heading = tk.Label(root, text="Choose your destination", font=heading_font)
destination_heading.pack(pady=10)

# frame 
frame = tk.Frame(root)
frame.pack(pady=5)

# Destination variable and options
destination_var = tk.StringVar()

destination = tk.Entry(frame, textvariable=destination_var, font=("Helvetica", 14), width= 25)
destination.pack(side="left", pady=10)


# Chose destination button
def choose_destination():
    output = filedialog.askdirectory()
    destination_var.set(output)

destination_button = tk.Button(frame, text="Choose Destination", command=choose_destination, font=("Helvetica", 12))
destination_button.pack(side="left", padx=10)

# Submit button
submit_button = tk.Button(root, text="Convert", command=Link_converter, font=("Helvetica", 14)) 
submit_button.pack(pady=10)

root.mainloop()