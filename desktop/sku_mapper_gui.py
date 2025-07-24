import tkinter as tk
import traceback
from tkinter import filedialog, ttk
import pandas as pd
import sys
import sys
import os

# Add ../backend to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from processor import map_skus



class SKUMappingTool:
    def __init__(self, master):
        self.master = master
        master.title("SKU to MSKU Mapper - Warehouse Tool")
        master.geometry("700x400")

        self.status = tk.Label(master, text="Upload an Excel file to begin", fg="blue")
        self.status.pack(pady=10)

        self.upload_btn = ttk.Button(master, text="Load Excel File", command=self.load_file)
        self.upload_btn.pack(pady=5)

        self.export_btn = ttk.Button(master, text="Export Mapped File", command=self.export, state=tk.DISABLED)
        self.export_btn.pack(pady=5)

        self.result_df = None

    def load_file(self):
        file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file:
            try:
                self.result_df = map_skus(file)
                mapped_count = self.result_df['Mapped SKU'].ne("Not Mapped").sum()
                total = len(self.result_df)
                self.status.config(
                    text=f"Mapped {mapped_count} of {total} rows ({round(mapped_count / total * 100, 2)}%)",
                    fg="green"
                )
                self.export_btn.config(state=tk.NORMAL)
            except Exception as e:
                traceback.print_exc()
                self.status.config(text=f"Error: {e}", fg="red")

    def export(self):
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if path:
            try:
                self.result_df.to_excel(path, index=False)
                self.status.config(text="File exported successfully", fg="green")
            except Exception as e:
                traceback.print_exc()
                self.status.config(text=f"Export failed: {e}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = SKUMappingTool(root)
    root.mainloop()
