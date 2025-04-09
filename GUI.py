import FileSystem as fs;
#import PyInstaller as PI;
import AutoCommenterAI as ac;
import customtkinter as ctk;
from customtkinter import filedialog;

def CreateGUI():
    window = ctk.CTk()
    window.title("Code Auto Commenter")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window.geometry("800x520")
    lable = ctk.CTkLabel(window, text="AI Code Commenter", anchor="center")
    lable.pack()
    
    filePath = ctk.CTkEntry(window, width=500)
    filePath.pack(pady=10)
    
    selectFile = ctk.CTkButton(window, text="Select File", command=lambda: SelectFile(filePath))
    selectFile.pack()
    
    display = ctk.CTkTextbox(window, wrap="word", text_color="orange")
    display.pack(pady=10, padx=20, fill="both", expand=True)
    
    displayBtn = ctk.CTkButton(window, text="Display selected file", command=lambda: DisplayFile(filePath.get(), display))
    displayBtn.pack()
    
    AIComment = ctk.CTkButton(window, text="Comment file", command=AIAutoCommenter)
    AIComment.pack()
    
    downloadBtn = ctk.CTkButton(window, text="Download displayed file", command=download)
    downloadBtn.pack(pady=20)
    
    window.mainloop()

def SelectFile(pathTxt):
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    pathTxt.delete(0, ctk.END)
    pathTxt.insert(0, path)

def DisplayFile(filepath, display):
    if(filepath and display):
        # Remove old displayed content
        display.delete(1.0, ctk.END)
        
        try:
            with open(filepath, 'r') as file:
                display.insert(1.0, file.read())
                
        except Exception as e:
            display.insert(1.0, f"Error opening file: {e}")

def AIAutoCommenter():
    ac.AIComment()

def download():
    fs.downloadFile()

CreateGUI()