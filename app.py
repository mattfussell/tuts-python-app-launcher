import tkinter as tk
from tkinter import filedialog, Text
import os


# This is where everything will attach
root = tk.Tk()
apps = [] # create a list to store the executables

# load the apps from save.txt
if os.path.isfile('save.txt'):
  with open('save.txt', 'r') as f:
    tempApps = f.read()
    tempApps = tempApps.split(',')
    apps = [ x for x in tempApps if x.strip() ]


# add an app to the launcher
def addApp():

  # clear the frame of any previous entries
  for entry in frame.winfo_children():
    entry.destroy()


  # open explorer to select a file
  filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
  
  apps.append(filename) # append executables to the list
  
  # Create labels for each executable in the list and attach it to the frame
  for app in apps:
    label = tk.Label(frame, text=app, bg="gray")
    label.pack()


# run the applications
def runApps():
  for app in apps:
    os.startfile(app)


# sizing: where to attach it, height, width, and color
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack() # commit the settings

# create a container inside the canvas
frame = tk.Frame(root, bg="White")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) # x, y settings to center the frame

# buttons for functionality
openFile = tk.Button(root, text="Open File", padx=10, pady=5, 
                        fg="White", bg="#263D42", command=addApp)

openFile.pack() # attach the button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, 
                        fg="White", bg="#263D42", command=runApps)
runApps.pack() # attach the button

# make saved app list visible in frame
for app in apps:
  label = tk.Label(frame, text=app)
  label.pack()


# run the program
root.mainloop()

# save the apps list
with open('save.txt', 'w') as f:
  for app in apps:
    f.write(app + ',')