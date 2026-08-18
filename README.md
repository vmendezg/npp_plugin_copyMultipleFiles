# Multiple File Merger Script for Notepad++

This Python script is designed for the **Python Script** plugin in Notepad++. It allows users to quickly merge the contents of all currently open files into a single, unified document through an interactive popup interface, prefixing each content block with its original filename.

## 🚀 Features
* **Interactive Modal:** Prompts the user to specify a name for the output file before merging.
* **Filename Headers:** Dynamically extracts and inserts the original short filename (e.g., `hello.md`) right above its respective text.
* **Smart Filtering:** Automatically excludes the newly created result tab to avoid duplicate loops or self-copying.
* **Notepad++ Style Compliant:** Structured using strict hardware tabs for indentation and formatting guidelines inspired by the project's core best practices.

---

## 🛠️ Installation and Setup

### 1. Install Python Script Plugin
1. Open Notepad++.
2. Go to the top menu and select **Plugins** > **Plugins Admin**.
3. Search for **Python Script**, check its box, and click **Install**. 
4. Notepad++ will automatically restart.

### 2. Create the Script
1. Go to **Plugins** > **Python Script** > **New Script**.
2. Name your file `copyMultipleFiles.py` and click **Save**.
3. Paste the following production-ready source code into the file and save it (`Ctrl + S`):

---

## 💻 How to Use

1. Open all the files you want to merge as separate tabs in Notepad++.
2. Go to **Plugins** > **Python Script** > **Scripts**.
3. Click on **copyMultipleFiles.py**.
4. A popup window will prompt you to enter a filename. Type your preferred name and click **OK**.
5. A brand new tab containing all merged texts structured exactly as requested will instantly appear:
   ```text
   hello.txt
   hi
   goodbye.txt
   bye
   ```
6. Press `Ctrl + S` to save the newly generated file to your local storage.
