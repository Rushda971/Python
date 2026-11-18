import tkinter as tk
from tkinter import filedialog

def save_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"),("All files", "*.*")])
    if file_path:
            try:
                with open(file_path, "w") as file:
                    # Assuming 'text_widget' is your Text widget
                    data_to_save = text_widget.get("1.0", tk.END)
                    file.write(data_to_save)
                print(f"Data saved to {file_path}")
            except Exception as e:
                print(f"Error saving file: {e}")

    # Example Tkinter setup (assuming you have a text_widget)
root = tk.Tk()
text_widget = tk.Text(root)
text_widget.pack()
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()
root.mainloop()