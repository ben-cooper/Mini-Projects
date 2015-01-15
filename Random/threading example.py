from threading import Thread
import time


def task1():
    time.sleep(2)
    print('first task complete')
def task2():
    time.sleep(1)
    print('second task complete')

#this block calls the functions in the correct order
print('Round 1 (without threading)')
task1()
task2()
print('third task complete')
print('')
#this block calls the functions in the same order but with threading instead
print('Round 2 (with threading)')
Thread(target=task1).start()
Thread(target=task2).start()
print('third task complete')
