# AICodeCommenter

This is a user-friendly Python app that uses local AI models to analyze and auto-generate helpful comments for Python code. Simply select a `.py` file using the GUI, click the **AI Comment** button, and the app will inject human-readable explanations directly into the code.

Built with a clean, modern interface using `tkinter` and `customtkinter`, the app is packaged as a Windows executable for ease of use — only an ollama instalation is required.

---

## Features

* **Select `.py` Files** – Load any Python script into the app via the GUI.
* **AI-Powered Commenting** – Leverages a locally running LLM (e.g., `codellama:7b` via Ollama) to generate useful, descriptive comments.
* **Save Updated Code** – Save the modified, commented version of the file with one click & a folder select.
* **Modern GUI** – Built with `tkinter` and `customtkinter` for a polished user experience.
* **Runs as Executable** – Packaged with `PyInstaller` for Windows. No need to install Python. Only need to install ollama.

---

## Technologies Used

* **Python 3.11**
* **CodeLlama (via Ollama)**
* **tkinter** / **customtkinter**
* **PyInstaller**

---

## Getting Started

### Option 1: Clone and Run with Python

```bash
git clone https://github.com/MikePerez2022/AIAutoCommenter.git
cd AIAutoCommenter
python Application.py
```

Make sure you have:

* Python 3.11 installed
* Ollama running (`ollama run codellama:7b`)

---

### Option 2: Run the Standalone Executable

1. Download the pre-built `.exe` file from the [Releases](#) (link placeholder).
2. Double-click to launch the app.
3. **Note:** Ollama must be installed and running. You can get it from [https://ollama.com](https://ollama.com).

---

## How to Use

1. **Select File** – Choose a `.py` file through the GUI.
2. **Load File** – Click the **Load** button to display the code in the editor.
3. **AI Comment** – Click the **AI Comment** button to auto-generate comments.
4. **Save Output** – Click the **Download** button and choose where to save the updated file.

   * To overwrite the original file, select the same directory.

---

## Requirements

* **Windows OS**
* **Ollama installed and running with `codellama:7b`**

  ```bash
  ollama run codellama:7b
  ```
