#!/bin/python3

from tkinter import *
from tkinter import messagebox
import pyperclip

def proccess_mac(mac_in):
    mac_out = ""
    split_char = ''
    mac_ary = []
    final_mac_ary = []
    mac_in = mac_in.strip()

    # check separator
    if ":" in mac_in:
        split_char = ':'
    elif "-" in mac_in:
        split_char = '-'
    elif len(mac_in) == 12:
        # handle scanned MAC's e.g. F0189884EA51
        tmp = '-'.join(mac_in[i:i + 2] for i in range(0, len(mac_in), 2))
        mac_in = tmp
        split_char = '-'
    else:
        messagebox.showerror("Error", "Enter a MAC Address that contains a : or -")
        return 1

    # create mac addr array 
    mac_ary = mac_in.split(split_char)

    if len(mac_ary) != 6:
        messagebox.showerror("Error", "Make sure the MAC is valid!")
        return 1

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
        #print("Got: " + mac_txt)
        mac = proccess_mac(mac_txt)
        if mac != 1:
            pyperclip.copy(mac)
            #root.clipboard_clear()
            #root.update()
            #root.clipboard_append(mac)
            #root.update()
            messagebox.showinfo(title="Your new MAC", message=(mac + " has been set on your clipboard"))
            mac_entry.delete(0,END)
            mac_entry.insert(0,mac)
            mac_entry.selection_range(0, END)
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
