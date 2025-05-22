from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
import tkinter as tk

def apply_syntax_highlighting(display, code):
    # Clear existing tags
    for tag in display.tag_names():
        display.tag_remove(tag, "1.0", tk.END)

    display.delete("1.0", tk.END)
    for ttype, value in lex(code, PythonLexer()):
        tag = "default"

        # Match broader token categories correctly
        if str(ttype).startswith("Token.Keyword"):
            tag = "keyword"
        elif str(ttype).startswith("Token.Name.Function"):
            tag = "function"
        elif str(ttype).startswith("Token.Comment"):
            tag = "comment"
        elif str(ttype).startswith("Token.Literal.String"):
            tag = "string"
        elif str(ttype).startswith("Token.Literal.Number"):
            tag = "number"
        elif str(ttype).startswith("Token.Operator"):
            tag = "operator"

        display.insert(tk.END, value, tag)

def configure_tags(display):
    # Configure colors (adjust to match VS Code’s theme)
    display.tag_configure("keyword", foreground="#569CD6")
    display.tag_configure("function", foreground="#DCDCAA")
    display.tag_configure("comment", foreground="#6A9955")
    display.tag_configure("string", foreground="#CE9178")
    display.tag_configure("number", foreground="#B5CEA8")
    display.tag_configure("operator", foreground="#D4D4D4")
    display.tag_configure("default", foreground="white")  # fallback
