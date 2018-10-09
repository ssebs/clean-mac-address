#!/bin/python3

from tkinter import *
from tkinter import messagebox

def proccess_mac(mac_in):
    mac_out = ""

    
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
