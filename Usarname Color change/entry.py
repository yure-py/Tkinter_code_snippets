import tkinter as tk
import re


def updating(*args):
    valor = entry_username_var.get()

    digit = bool(re.search("[0-9]", valor))
    special = bool(re.search("[@#$\- _]", valor))
    lenght = True if len(valor) >= 8 else False

    label_condition1["fg"] = "green" if digit else "red"
    label_condition2["fg"] = "green" if special else "red"
    label_condition3["fg"] = "green" if lenght else "red"


root = tk.Tk()
root.title("Username color verify")
root.geometry("+1000+500")

# Frame & label username
frame_username = tk.Frame(root, pady=5)
label = tk.Label(frame_username, text="Username: ")

# Entry username
entry_username_var = tk.StringVar()
entry_username = tk.Entry(frame_username, textvariable=entry_username_var)
entry_username_var.trace_add("write", updating)

# Validation configuration
frame_validation = tk.Frame(root, pady=5, padx=5, bd=4, relief="ridge")

# conditions label's
label_validation = tk.Label(frame_validation, text="Must contain at least:")
label_condition1 = tk.Label(frame_validation, text="One Digit Characters", fg="red")
label_condition2 = tk.Label(frame_validation, text="One Special Characters", fg="red")
label_condition3 = tk.Label(frame_validation, text="8 or more Characters", fg="red")

# grids
label.grid(row=0, column=0)
frame_username.grid()
entry_username.grid(row=0, column=1, padx=5, sticky="we")
frame_validation.grid(row=3, columnspan=2, sticky="we")
label_validation.grid(sticky="w")
label_condition1.grid(sticky="we", ipadx=50)
label_condition2.grid()
label_condition3.grid()

root.mainloop()
