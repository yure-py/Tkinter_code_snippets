import tkinter as tk
from tkinter import ttk


class Settings:
    def __init__(self):
        self.comboboxes = {
            "width": 3,
            "font": ("Arial", 18),
            "state": "readonly",
            "justify": "center",
            "values": [f"0{x}" if x < 10 else str(x) for x in range(24)],
        }
        self.button = {
            "bg": "white",
            "relief": "solid",
        }
        self.labels = {
            "text": ":",
            "font": ("Arial", 12),
            "relief": "flat",
            "bg": "white",
        }

        self.var1 = tk.StringVar(value="00")
        self.var2 = tk.StringVar(value="00")
        self.var3 = tk.StringVar(value="00")

        self.style = ttk.Style()
