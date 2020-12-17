from tkinter import *

import tkinter.filedialog

import tkinter.messagebox

from tkinter.colorchooser import askcolor

import datetime

import webbrowser

from tkinter.filedialog import askopenfilename, asksaveasfilename

from os import path

def line():

    line = "_" * 80

    text.insert(INSERT,line)

    

def date():

    date = datetime.date.today()

    text.insert(INSERT,date)

   

def normal():

    text.config(font = ("Arial", 10))



def bold():

    text.config(font = ("Arial", 10, "bold"))



def underline():

    text.config(font = ("Arial", 10, "underline"))



def italic():

    text.config(font = ("Arial",10,"italic"))

    

def font():
    global count
    color = askcolor()
    if text.tag_ranges('sel'):
        text.tag_add('colortag_' + str(count), SEL_FIRST,SEL_LAST)
        text.tag_configure('colortag_' + str(count), foreground=color[1])
        count += 1
    else:
        text.config(foreground=color[1])



def end():

    root.destroy()



def about():

    pass



def openn():

    text.delete(1.0 , END)

    file = open(askopenfilename() , 'r')

    txt = file.read()

    text.insert(INSERT,txt)

   

    

def save():

    namef = asksaveasfilename()

    if namef:

        alltext = text.get(1.0, END)                      

        open(namef, 'w').write(alltext) 



def copy():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get()) 



def paste():

    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Error","The notes are empty")



def clear():

    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)



def clearall():

    text.delete(1.0 , END)



def background():

    (triple,color) = askcolor()

    if color:

       text.config(background=color)
        

       

def about():

    ab = Toplevel(root)

    txt = "Textpad\n Text Editor\n Developed by:\n Mustak,Manshi,Tridib and Ikramul"

    la = Label(ab,text=txt,foreground='blue')

    la.pack()

    

def web():

    webbrowser.open('http://www.google.com')





root = Tk()

root.title("Textpad")

menu = Menu(root)

count=0

filemenu = Menu(root)

root.config(menu = menu)

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open...", command=openn)

filemenu.add_command(label="Save...", command=save)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=end)



modify = Menu(root)

menu.add_cascade(label="Edit",menu = modify)

modify.add_command(label="Copy", command = copy)

modify.add_command(label="Paste", command=paste)

modify.add_separator()

modify.add_command(label = "Clear Selected", command = clear)

modify.add_command(label = "Clear All", command = clearall)







insertmenu = Menu(root)

menu.add_cascade(label="Insert",menu= insertmenu)

insertmenu.add_command(label="Date",command=date)

insertmenu.add_command(label="Line",command=line)






        

formatmenu = Menu(menu)

menu.add_cascade(label="Format",menu = formatmenu)

formatmenu.add_cascade(label="Color...", command = font)

formatmenu.add_separator()

formatmenu.add_radiobutton(label='Normal',command=normal)

formatmenu.add_radiobutton(label='Bold',command=bold)

formatmenu.add_radiobutton(label='Underline',command=underline)

formatmenu.add_radiobutton(label='Italic',command=italic)



personalize = Menu(root)

menu.add_cascade(label="Customize",menu=personalize)

personalize.add_command(label="Background", command=background)

                 

helpmenu = Menu(menu)

menu.add_cascade(label="Additional", menu=helpmenu)

helpmenu.add_command(label="Info", command=about)

helpmenu.add_command(label="Search Engine", command = web)


text = Text(root, height=40, width=80, font = ("Arial", 16))



sb = Scrollbar(root, command=text.yview)

sb.config(command=text.yview)                  

text.config(yscrollcommand=sb.set)           

sb.pack(side=RIGHT, fill=Y)

text.pack()





root.resizable(0,0)

root.mainloop()
