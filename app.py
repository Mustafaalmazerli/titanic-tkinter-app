import tkinter as tk
from tkinter import ttk, messagebox
from read import read_data
from process import process_data

class TitanicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Titanic Data Viewer")
        self.root.geometry("800x600")

        # GUI layout
        self.create_widgets()

    def create_widgets(self):
        # File path label and entry
        self.file_label = tk.Label(self.root, text="CSV File Path:")
        self.file_label.pack(pady=5)
        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.pack(pady=5)
        self.file_entry.insert(0, 'C:/Users/musta/OneDrive/Skrivbord/ds23_f-rdjupad_python-main/kunskapskontroll_2/train.csv')

        self.icon = tk.PhotoImage(file="C:/Users/musta/OneDrive/Skrivbord/ds23_f-rdjupad_python-main/kunskapskontroll_2/cat.png")  
        self.icon = self.icon.subsample(5, 5)
        # Skapa knappen med ikonen och text
        self.run_button = tk.Button(
            self.root, 
            text="Process to load", 
            image=self.icon,         
            compound="left",         
            command=self.run_process,  
            width=300, height=200,   
            bg="yellow", fg="black",  
            padx=10, pady=10    
        )       
        self.run_button.pack(pady=20)


        # Treeview for displaying data
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(pady=20, fill='both', expand=True)

        # Scrollbars for Treeview
        self.tree_scroll_y = tk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree_scroll_y.pack(side="right", fill="y")
        self.tree_scroll_x = tk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)
        self.tree_scroll_x.pack(side="bottom", fill="x")
        self.tree.configure(yscrollcommand=self.tree_scroll_y.set, xscrollcommand=self.tree_scroll_x.set)

        # Text widget for log messages
        self.log_text = tk.Text(self.root, height=5, width=20)
        self.log_text.pack(pady=10)

    def run_process(self):
        file_path = self.file_entry.get()

        try:
            # Read data
            df = read_data(file_path)
            self.log_message()

            # Process and filter data
            processed_data = process_data(df)
            self.log_message()

            # Display data in the Treeview
            self.display_data(processed_data)

        except Exception as e:
            self.log_message()  
            messagebox.showerror("Error", f"An error tänke om: {e}")
            # ett felmeddelande
    def log_message(self):
        
        self.log_text.insert(tk.END, "Bra jobbet koden fungerar utan Error\n")
        self.log_text.see(tk.END)  

    def display_data(self, df):
        # Clear existing data in Treeview
        self.tree.delete(*self.tree.get_children())

        # Set up the columns and headers based on DataFrame columns
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="w")

        # Insert the data into Treeview
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))


root = tk.Tk()
app = TitanicApp(root)
root.mainloop()
