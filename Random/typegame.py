from random import randint
from tkinter import *
#from tkinter.ttk import *


def first_run(event):
    root.bind('<Key>', wrong_key)
    new_letter('<Return>')
    timer()


def timer():
    info['time'] += 1
    if info['time'] != 0:
        speedtext.set('Avg Speed: ' + str(info['correct'] / info['time'])[:4] +
                      ' correct strokes/second')
    root.after(1000, timer)


def new_letter(old_char):
    info['score'] += 1
    info['correct'] += 1
    info['tries'] += 1
    info['key_num'] += 1
    if info['tries'] != 0:
        scoretext.set('Score: ' + str(
            info['score']) + '   ' + 'Accuracy: ' + str(
                info['correct'] / info['tries'] * 100)[:4] + '%')
    root.unbind(old_char)
    root.bind(old_char, wrong_key)
    x = chr(randint(97, 122))
    root.bind(x, lambda event: new_letter(x))
    root.bind(x.upper(), lambda event: new_letter(x))
    letter.set('Key ' + str(info['key_num']) + ':      ' + x)


def wrong_key(event):
    if info['score'] != 0:
        info['score'] -= 1
    info['tries'] += 1
    scoretext.set('Score: ' + str(info['score']) + '   ' + 'Accuracy: ' + str(
        info['correct'] / info['tries'] * 100)[:4] + '%')

root = Tk()
root.bind('<Return>', first_run)
root.title('Typing Game')
root.geometry('220x60')
root.resizable(0, 0)
letter = StringVar()
scoretext = StringVar()
speedtext = StringVar()
info = {'score': -1, 'correct': -1, 'tries': -1, 'key_num': 0, 'time': -1}
scoretext.set('Score: n/a' + '   ' + 'Accuracy: n/a')
letter.set('Press Enter')
speedtext.set('Avg Speed: n/a')
cur_let = Label(root, textvariable=letter)
cur_score = Label(root, textvariable=scoretext)
cur_speed = Label(root, textvariable=speedtext)
cur_let.pack()
cur_score.pack()
cur_speed.pack()
root.mainloop()
