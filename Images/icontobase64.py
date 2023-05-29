# -*- coding:utf -8 -*-
__version__ = '1.0'
import base64
from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.title("Icon to base64 " +str(__version__))
root.resizable(width=False, height=False)
root.geometry("380x250+300+300")
calculated_text = Text(root,height=15, width=50)

myFormats = [
    ('TXT files','*.txt'),
    ('HTML files','*.html;.htm'),
    ('All files','*.*'),  
    ]

def insertImg():
    file_name = fd.askopenfilename()
    f = open(file_name, 'rb')
    s = f.read()
    calculated_text.insert('1.0',(str(base64.b64encode(s))[2:])[:-1])
    f.close()

def extractText():
    file_name = fd.asksaveasfilename(parent=root,filetypes=myFormats,defaultextension='')
    f = open(file_name, 'w')
    s = calculated_text.get(1.0, END)
    f.write(s)
    f.close()  
   
def erase():  
    calculated_text.delete('1.0', END)
   
b1 = Button(text="Open",command=insertImg)
b1.grid(row=3, column=0, sticky=E, padx=5, pady=8,)
b2 = Button(text="Save", command=extractText)
b2.grid(row=3, column=1, sticky=E, padx=5, pady=8,)
erase_button = Button(text="Clear", command=erase)
erase_button.grid(row=3, column=2, padx=35, pady=8, sticky="W")

scrollb = Scrollbar(root, command=calculated_text.yview)
scrollb.grid(row=4, column=4, sticky='nsew')
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)
calculated_text.configure(yscrollcommand=scrollb.set)
       
root.mainloop()