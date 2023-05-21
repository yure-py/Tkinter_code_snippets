import tkinter as tk
import re


def updating(character_input, string):
    valor = string

    digit = bool(re.search("[0-9]", valor))
    special = bool(re.search("[@#$\- _]", valor))
    lenght = True if len(valor) >= 8 else False

    label_condition1["fg"] = "green" if digit else "red"
    label_condition2["fg"] = "green" if special else "red"
    label_condition3["fg"] = "green" if lenght else "red"

    print(valor)
    return bool(re.match("[^ ]", character_input))


root = tk.Tk()
root.title("Username color verify")
root.geometry("+1000+500")

# username
frame_username = tk.Frame(root, pady=5)
label_usarname = tk.Label(frame_username, text="Username: ")

entry_username_var = tk.StringVar()
entry_username = tk.Entry(frame_username, textvariable=entry_username_var,
                          validate="key", validatecommand=(root.register(updating), "%S", "%P"))

# Color condtitions
frame_validation = tk.Frame(root, pady=5, padx=5, bd=4, relief="ridge")

label_validation = tk.Label(frame_validation, text="Must contain at least:")
label_condition1 = tk.Label(frame_validation, text="One Digit Characters", fg="red")
label_condition2 = tk.Label(frame_validation, text="One Special Characters", fg="red")
label_condition3 = tk.Label(frame_validation, text="8 or more Characters", fg="red")

# grids
frame_username.grid()
label_usarname.grid(row=0, column=0)  # contido no frame usarname
entry_username.grid(row=0, column=1, padx=5)

frame_validation.grid(row=3, columnspan=2)
label_validation.grid(sticky="w")
label_condition1.grid(sticky="we", ipadx=50)
label_condition2.grid()
label_condition3.grid()

root.mainloop()
