#!/bin/python3

from tkinter import *
from tkinter import messagebox

def proccess_mac(mac_in):
    mac_out = ""
    split_char = ''
    mac_ary = []
    final_mac_ary = []
    mac_in = mac_in.strip()

    # check seperator
    if ":" in mac_in:
        split_char = ':'
    elif "-" in mac_in:
        split_char = '-'
    else:
        messagebox.showerror("Error", "Enter a MAC Address that contains a : or -")

    # create mac addr array 
    mac_ary = mac_in.split(split_char)

    if len(mac_ary) != 6:
        messagebox.showerror("Error", "Make sure the MAC is valid!")

    # remove leading 0 + lowercase
    for x in mac_ary:
        tmp = x.lower()
        if tmp.startswith("0"):
            tmp = tmp[1]
        final_mac_ary.append(tmp)

    for x in final_mac_ary:
        mac_out += x + ":"
    mac_out = mac_out[:-1]
    
    return mac_out
# end process_mac

def handle_return(event):
    mac_txt = ""
    mac_txt = mac_entry.get()

    if mac_txt != "":
        print("Got: " + mac_txt)
        proccess_mac(mac_txt)
    else:
        messagebox.showerror("Error", "Enter a MAC Address")
# end handle_return


# root TK obj
root = Tk()

# add label
lab1 = Label(root, text="Input your MAC Address: ")
lab1.pack(side=LEFT)

# add entry
mac_entry = Entry(root, bd=5)
mac_entry.bind("<Return>",handle_return)
mac_entry.pack(side=RIGHT)
mac_entry.focus()

# run mainloop
root.title = "Clean MAC"
root.mainloop()
