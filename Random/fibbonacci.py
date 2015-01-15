import os #This library allows us to change the directory and use Dos commands (like for 'cls' which clears the screen)
def calculate_sequence(path,counter): #This is the function the calculates the fibonacci sequence and then outputs it to a file
    """
    (str,int) -> bool
    Return true iff parameters were valid (after outputting sequence to file if they were true)
    >>> calculate_sequence("C:\\Users\\ben",20)
    True
    >>> calculate_sequence("Hello",-5)
    False
    """
    value1 = 0 #this keeps track of the previous number
    value2 = 1 #this keeps track of the current number
    try: #This tries to use the specified path and counter value
        os.chdir(path)
        counter = int(counter)
        if counter <= 0:
            raise Exception()
    except: #If their inputs aren't valid then the code will exit and return a value of false
        if path != 0: #If path is still an integer then the user has not entered paramemters.
            #So the program should not tell the user that they were invalid
            print("You have entered invalid parameters!")
            print()
        return False
    else: #This code runs if the inputs are valid
        file = open('fibonacci.txt', 'w') #First we create a file for the purpose of outputting the sequence (writing)
        file.write("This is " + str(counter) + " terms the the fibonacci sequence." + "\r\n" + "\r\n")
        file.write("1")
        while counter != 1: #This loop calculates fibonacci numbers until the required amount (specified by the user) is reached
            #The loop stops when the counter is 1 because the first term is directly appended to the file
            os.system('cls')
            print("Terms left: " + str(counter - 1))
            value3 = value2 + value1
            result = ", " + str(value3)
            file.write(result) #The result 'result' is then written to the file
            value1 = value2 #Here we are incrementing the sequence and the loop counter 'counter
            value2 = value3
            counter = counter - 1
        print("Done!")
        os.system('pause')
        return True #This lets the program know the function was successful
path = 0  #These are the default values for the user's input
counter = 0
os.system('title Fibonacci Sequence')
while calculate_sequence(path,counter) == False: #This loop continues to ask the user for inputs until it recieves valid inputs  
    path = input("Please enter the location you would like the output to be (use double slashes): ")
    counter = input("Please enter the amount of fibonacci numbers you'd like to generate: ")
    os.system('cls') #This clears the screen