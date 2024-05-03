import tkinter as tk
from tkinter import filedialog
import os

class FolderSelectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Folder Selection")

        self.label = tk.Label(master, text="Select a folder:")
        self.label.pack(pady=10)  # Adding padding in the y-axis

        self.select_button = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=5)  # Adding padding in the y-axis
        
        self.selected_folder = None
        self.selected_label = tk.Label(master, text="")
        self.selected_label.pack(pady=10)  # Adding padding in the y-axis

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=5)  # Adding padding in the y-axis
        
    
    def convert_size(self, size_bytes):
        # Size conversion constants
        KB = 1024.0
        MB = KB * KB
        GB = MB * KB
        TB = GB * KB
        # Convert bytes to appropriate size
        if size_bytes >= TB:
            return "{:.2f} TB".format(size_bytes / TB)
        elif size_bytes >= GB:
            return "{:.2f} GB".format(size_bytes / GB)
        elif size_bytes >= MB:
            return "{:.2f} MB".format(size_bytes / MB)
        elif size_bytes >= KB:
            return "{:.2f} KB".format(size_bytes / KB)
        else:
            return "{:.2f} bytes".format(size_bytes)    
        
    def get_folder_size(self, folder_path):
        total_size = 0
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        # Convert size to human-readable format
        return self.convert_size(total_size)

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        print("Selected Folder:", self.selected_folder)
        size = self.get_folder_size(self.selected_folder)
        self.selected_label.config(text=f"Selected Folder: {self.selected_folder}\nFolder Size: {size}")

    def submit(self):
        if self.selected_folder:
            print("Submit action with folder:", self.selected_folder)
            # You can add your code here to do something with the selected folder
        else:
            print("Please select a folder first.")

def main():
    root = tk.Tk()
    app = FolderSelectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
