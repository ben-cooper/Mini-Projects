'''
Ben's Binary Converter
Version Info: 1.1 beta

This program is designed to encrypt and decrypt messages to and from binary
with a GUI in tkinter.

Copyright (c) Ben Cooper 2013
Designed in PyScipter for python 3.3.2 and written according to PEP8
'''
from tkinter import *
from tkinter.ttk import *


def encrypt_message(input_str):
    '''(str) -> str
    Return input_str converted to binary form.
    REQ characters in input_str must have corresponding ASCII values
    >>> encrypt_message('hello')
    '01101000 01100101 01101100 01101100 01101111'
    '''
    #initalizing the encrypted message variable
    result = ''
    #first convert each letter into an ascii value and then convert the value
    # into binary
    for i in input_str:
        #we want to remove the 'b' that python adds to the binary version
        # we also want to add a space at the end of each binary block
        result += str(bin(ord(i))).replace('b', '') + ' '
    #removing the space at the end and returning result
    return result.strip()


def decrypt_message(input_str):
    '''(str) -> str
    Return input_str converted into normal form from binary form.
    REQ input_str must be a string of only binary numbers, binary numbers
    must be seperated by spaces, and each binary number must corresspond to a
    valid ascii value (<110000D)
    >>> decrypt_message('01101000 01100101 01101100 01101100 01101111')
    'hello'
    '''
    #initializing the decrypted message variable
    result = ''
    #checking if input_str is valid
    if set(input_str) <= set('10 '):
        #setting each block of binary numbers into a list
        letter_list = input_str.split()
        #initializing index value and error boolean
        index = 0
        error = False
        #converting each element in letter_list (binary blocks) to decimal
        # and then into characters to add to result
        while index < len(letter_list) and not error:
            if len(letter_list[index]) <= 16:
                result += chr((int(letter_list[index], 2)))
                index += 1
            else:
                #stops the loop and returns an error if a binary block is too
                # long
                error = True
                result = 'Invalid binary value!'
    else:
        result = 'Invalid binary string!'
    return result


def clear_text():
    '''() -> NoneType
    This function clears both text boxes (entries) in the GUI of the program
    '''
    inputval.set('')
    output.set('')


def copy_all():
    '''() -> NoneType
    This function clears the clipboard and then adds the output text from the
    GUI to the clipboard so the user can paste the message
    '''
    root.clipboard_clear()
    root.clipboard_append(output.get())

if __name__ == '__main__':
    #here we are creating the interface if the program is not being imported
    root = Tk()
    root.title("Ben's Binary Converter")
    root.resizable(1, 0)
    root.minsize(height=75, width=420)
    root.columnconfigure(4, weight=1)
    #these are the texts for outputtext and inputbox
    inputval = StringVar()
    output = StringVar()
    #creating the widgets
    inputbox = Entry(root, textvariable=inputval)
    outputtext = Entry(root, textvariable=output)
    outputtext.configure(state='readonly')
    encrypt = Button(root, text='Encrypt', command=lambda: output.set(
        encrypt_message(inputbox.get())))
    decrypt = Button(root, text='Decrypt', command=lambda: output.set(
        decrypt_message(inputbox.get())))
    copy = Button(root, text='Copy Output', command=copy_all)
    clear = Button(root, text='Clear', command=clear_text)
    inputlabel = Label(root, text='Input: ')
    outputlabel = Label(root, text='Output: ')
    #now we render the widgets
    inputlabel.grid(row=0, column=0, sticky=W)
    outputlabel.grid(row=1, column=0, sticky=W)
    inputbox.grid(row=0, column=1, columnspan=4, sticky=E+W)
    outputtext.grid(row=1, column=1, columnspan=4, sticky=E+W)
    encrypt.grid(row=2, column=1, sticky=W)
    decrypt.grid(row=2, column=2, sticky=W)
    copy.grid(row=2, column=3, sticky=W)
    clear.grid(row=2, column=4, stick=W)
    root.mainloop()
