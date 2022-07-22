from tkinter import filedialog
from tkinter import *
from zipfile import ZipFile
import os

try:
    os.mkdir(r'C:\\Unzip')
except OSError:
    pass

root = Tk()

def extract():
    folder = filedialog.askopenfilename()
    with ZipFile(folder, 'r') as zip:
        print("extraindo...")
        zip.extractall(r'C:\\Unzip')
        print("pronto!")


root.title('ClebsZip')
title = Label(text=" selecione seu arquivo abaixo ", fg="green", font=["", 17])
title.pack(anchor='center')
resultado = Label(text= "seu arquivo será extraído na pasta C:/Unzip assim que selecionado",fg="green", font=["", 15])
resultado.pack(side="bottom")
extract_button = Button(text="selecionar arquivo", bg= "lightgreen", font=15, command = extract)
extract_button.pack(side="bottom")


root.mainloop()