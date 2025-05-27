import customtkinter as ctk;
from customtkinter import filedialog as fd;
import TextColor as tc
import os;

def DownloadFileGUI(filename, contents):
    dir = fd.askdirectory(title="Select File download location")
    saveFile = dir + "/" + os.path.basename(filename)
    
    if(filename and contents):
        try:
            CreateFile(saveFile, contents)
        except FileExistsError as e:
            print(f"An error occured while creating a file {e}")
    else:
        print("No file is selected or there are no contents displayed")

def SelectFileGUI(pathTxt):
    path = fd.askopenfilename(filetypes=[("All Code Files", "*.py *.js *.html *.c *.cpp *.cs *.java")])
    pathTxt.delete(0, ctk.END)
    pathTxt.insert(0, path)

def DisplayFileGUI(filepath, display):
    if(filepath and display):
        display.delete(1.0, ctk.END)
        
        try:
            with open(filepath, 'r') as file:
                display.insert(1.0, file.read())
                tc.apply_syntax_highlighting(display, display.get(0.0, ctk.END))
        except Exception as e:
            display.insert(1.0, f"Error opening file: {e}")

def CreateFile(filepath, content):
    if filepath:
        if os.path.exists(filepath):
            print("This file already exsists")
        else:
            with open(filepath, 'w') as f:
                f.write(content)