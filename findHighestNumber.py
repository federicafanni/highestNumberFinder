def findTheHighest(*values): #Function max that takes an undetermined amount of values and returns the highest,
                             #(without using the in-built max function and creating my own)
    largestValue = None #Creating the variable for the largest value and setting it to none
                        #so as to have an initial value to compare the values of the list with.'''
    
    for value in values:#For each value in the group of values:
        if largestValue is None or largestValue < value:#if the largestValue variable is equal to None or 
                                                        #if it is smaller than the value (of the *values group) it is being compared to,
            largestValue = value                        #then assign to largestValue the value of the current value variable (that is, largetValue will no longer be equal to None
                                                        #because it will be assigned the new value of the value variable).
                                                        #The code above will be repeated for each value in the *values group and 
                                                        #everytime there is a value in the group that is higher than the current value assigned to largestValue,
                                                        #largestValue will have a new value assigned/will be updated.
    return largestValue 
    

if __name__ == "__main__":  
    print("WHAT'S THE LARGEST NUMBER?")
    while True: #Iterating until q is entered
        userInput= input('Enter some numbers (ex. 3 5 200) or enter q to quit: ')
        if userInput.lower() == "q": #If user types q or Q,
            break #exit the loop
        numbersSplit = userInput.split(" ")#splitting the numbers entered
        try: #Checking if the values entered are numbers
            #Converting and passing the split values as integers to the function
            numbers = list(map(int, numbersSplit))
            largest = findTheHighest(*numbers)
            print('The largest value is: ', largest)
        except ValueError:
            print('Invalid input. Enter valid integers.')

    print("Goodbye!")

