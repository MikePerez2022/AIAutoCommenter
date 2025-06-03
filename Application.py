import FileSystem as fs;
import AutoCommenterAI as ac;
import customtkinter as ctk;
import tkinter as tk;
import TextColor as tc
import threading

def CreateGUI():
    window = ctk.CTk()
    window.title("Code Auto Commenter")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window.geometry("1080x650")
    lable = ctk.CTkLabel(window, text="AI Code Commenter", anchor="center")
    lable.pack()
    
    filePath = ctk.CTkEntry(window, width=650)
    filePath.pack(pady=10)
    
    selectFile = ctk.CTkButton(window, text="Select File", command=lambda: fs.SelectFileGUI(filePath))
    selectFile.pack()
    
    text_frame = ctk.CTkFrame(window, corner_radius=25)
    text_frame.pack(padx=20, pady=10, fill="both", expand=True)
    
    display = tk.Text(text_frame, bg="#131313", fg="white", insertbackground="white", bd=0, highlightthickness=1,
    highlightbackground="#282828", font=("Consolas", 16), wrap="word")
    display.pack(fill="both", expand=True)
    tc.configure_tags(display)
    
    actions_frame = ctk.CTkFrame(window)
    actions_frame.pack(pady=10)
    
    displayBtn = ctk.CTkButton(actions_frame, text="Load selected file", command=lambda: fs.DisplayFileGUI(filePath.get(), display))
    displayBtn.grid(row=0, column=0, padx=5)
    
    AIComment = ctk.CTkButton(actions_frame, text="Comment file", command=lambda: CommentAndDisplay(display))
    AIComment.grid(row=0, column=1, padx=5)
    
    downloadBtn = ctk.CTkButton(actions_frame, text="Download displayed file", command=lambda: fs.DownloadFileGUI(filePath.get(), display.get(0.0, tk.END)))
    downloadBtn.grid(row=0, column=2, padx=5)
    
    window.mainloop()


def CommentAndDisplay(display):
    def strip_code_fences(text):
        text = text.strip()
        if text.startswith("'''") and text.endswith("'''"):
            return text[3:-3].strip()
        if text.startswith("```python") and text.endswith("```"):
            return text[9:-3].strip()
        if text.startswith("```") and text.endswith("```"):
            return text[3:-3].strip()
        return text

    def task():
        code = display.get(0.0, tk.END)
        filename = "file.py"  # Or get from filePath if available
        display.delete(1.0, tk.END)
        display.insert(tk.END, "Generating...\n")
        display.see(tk.END)
        last_chunk = ""
        for chunk in ac.comment_code(code):
            cleaned_chunk = strip_code_fences(chunk)
            last_chunk = cleaned_chunk
            def update_display(chunk=cleaned_chunk):
                display.delete(1.0, tk.END)
                display.insert(tk.END, chunk)
                tc.apply_syntax_highlighting(display, chunk, filename)
            display.after(0, update_display)
        def highlight_final():
            tc.apply_syntax_highlighting(display, last_chunk, filename)
            print("Display Updated")
        display.after(0, highlight_final)
    threading.Thread(target=task, daemon=True).start()


CreateGUI()