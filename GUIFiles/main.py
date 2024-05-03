import tkinter as tk
from tkinter import filedialog

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


    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        print("Selected Folder:", self.selected_folder)
        self.selected_label.config(text=f"Selected Folder: {self.selected_folder}")

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
