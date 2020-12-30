from tkinter import *
from tkinter.filedialog import *

def domenu( ):
    print("OK")

def openmenu( ):
    filename = askopenfilename(parent = root, filetypes = (("GIF 파일", "*.gif"),("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

root = Tk( )
root.geometry("400x400")
root.title("그림들")

photo = PhotoImage( )
pLabel = Label(root, image=photo)
pLabel.pack(expand=1, anchor = CENTER)

menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label = "File" , menu=filemenu)
filemenu.add_command(label="New", command=domenu)
filemenu.add_command(label="Open", command=domenu)
filemenu.add_command(label="Save", command=domenu)
filemenu.add_command(label="Save as...", command=domenu)
filemenu.add_separator( )
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=domenu)
editmenu.add_command(label="Paste", command=domenu)
editmenu.add_separator( )
editmenu.add_command(label="Delete", command=domenu)

helpmenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=domenu)

root.cofig(menu=menubar)
root.mainloop( )




