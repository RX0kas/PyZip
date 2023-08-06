import tkinter as tk
from tkinter import ttk, filedialog
import zipfile

def unZip(file, destination):
    with zipfile.ZipFile(file, 'r') as fichierzip:
        fichierzip.printdir() 
  
        # extraction of all the files
        print('extraction...')
        for info in fichierzip.infolist():
            try:
                fichierzip.extract(info.filename, destination)
                print(f"{info.filename} - {info.file_size} bytes")
            except UnicodeDecodeError:
                # Ignore non-decodable characters in the filename
                print(f"Warning: Could not extract '{info.filename}' due to filename encoding issue.")
    print('Terminé!')

def browse_zip_file():
    file_path = filedialog.askopenfilename(title="Select ZIP file", filetypes=[("ZIP files", "*.zip")])
    if file_path:
        zip_file_entry.delete(0, tk.END)
        zip_file_entry.insert(tk.END, file_path)

        # Clear the listbox
        file_listbox.delete(0, tk.END)

        # Update the listbox with ZIP contents
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            for info in zip_file.infolist():
                file_listbox.insert(tk.END, f"{info.filename} - {info.file_size} bytes")

def browse_destination_folder():
    folder_path = filedialog.askdirectory(title="Select destination folder")
    if folder_path:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(tk.END, folder_path)

def extract_zip():
    zip_file_path = zip_file_entry.get()
    destination_folder = destination_entry.get()

    if zip_file_path and destination_folder:
        unZip(zip_file_path, destination_folder)
        result_label.config(text="Extraction complete.")
    else:
        result_label.config(text="Please select both ZIP file and destination folder.")

# Create the main application window
root = tk.Tk()
root.title("PyZip")
root.iconbitmap("D:\Programme\PyZip\Logo.ico")

# Style
style = ttk.Style()
style.theme_use("xpnative")  # Change this to any available theme ('clam', 'default', 'alt', 'vista', 'xpnative', 'classic')

# Layout
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")

# Widgets
zip_file_label = ttk.Label(frame, text="Select ZIP file:")
zip_file_label.grid(row=0, column=0, padx=5, pady=5)

zip_file_entry = ttk.Entry(frame, width=40)
zip_file_entry.grid(row=0, column=1, padx=5, pady=5)

zip_file_button = ttk.Button(frame, text="Browse", command=browse_zip_file)
zip_file_button.grid(row=0, column=2, padx=5, pady=5)

file_listbox = tk.Listbox(frame, width=70, height=10)
file_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

destination_label = ttk.Label(frame, text="Select destination folder:")
destination_label.grid(row=2, column=0, padx=5, pady=5)

destination_entry = ttk.Entry(frame, width=40)
destination_entry.grid(row=2, column=1, padx=5, pady=5)

destination_button = ttk.Button(frame, text="Browse", command=browse_destination_folder)
destination_button.grid(row=2, column=2, padx=5, pady=5)

extract_button = ttk.Button(frame, text="Extract ZIP", command=extract_zip)
extract_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

result_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Adjust row and column weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Run the main event loop
root.mainloop()
