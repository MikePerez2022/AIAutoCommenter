from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
import tkinter as tk
from pygments.lexers import get_lexer_for_filename, guess_lexer
from pygments.util import ClassNotFound

def apply_syntax_highlighting(display, code, filename):
    lexer = get_lexer(filename, code)
    
    # Clear existing tags
    for tag in display.tag_names():
        display.tag_remove(tag, "1.0", tk.END)

    display.delete("1.0", tk.END)
    for ttype, value in lex(code, lexer):
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

def get_lexer(filename, code=None):
    try:
        # Try to get lexer from filename extension
        lexer = get_lexer_for_filename(filename)
    except ClassNotFound:
        if code:
            # Fallback: guess lexer from code content if available
            lexer = guess_lexer(code)
        else:
            # Fallback to plain text lexer if no better option
            from pygments.lexers import TextLexer
            lexer = TextLexer()
    return lexer
