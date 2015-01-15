import os
import shutil
import time
from tkinter import *


def backup_cycle(filepath, savepath, seconds):
    if savepath != '':
        counter = 0
        os.chdir(savepath)
        os.system('md Minebackup')
        savepath += '\\Minebackup'
        os.chdir(savepath)
        seconds = int(seconds)
        while True:
            counter += 1
            num.set('Current Backup: ' + str(counter))
            root.update_idletasks()
            curpath = 'Backup' + str(counter) + time.strftime("%I:%M")
            shutil.copytree(filepath, curpath)
            time.sleep(seconds)
root = Tk()
root.geometry("600x100")
root.resizable(0, 0)
root.columnconfigure(1, weight=1)
num = StringVar()
num.set('Current Backup: 0')
root.title('Minebackup')
filel = Label(root, text='World Path: ')
filet = Entry(root)
savel = Label(root, text='Backup Path: ')
savet = Entry(root)
timel = Label(root, text='Interval (seconds): ')
timet = Entry(root)
currnum = Label(root, textvariable=num)
startbut = Button(root, text='Start Cycle!', command=backup_cycle(filet.get(),
                                                                  savet.get(),
                                                                  timet.get()))
filel.grid(row=0)
filet.grid(row=0, column=1, sticky=E+W)
savel.grid(row=1)
savet.grid(row=1, column=1, sticky=E+W)
timel.grid(row=2)
timet.grid(row=2, column=1, sticky=W)
startbut.grid(row=3)
currnum.grid(row=3, column=1)
root.mainloop()
