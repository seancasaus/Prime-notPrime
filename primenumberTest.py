"""---------------------------------------------------------------------------------------------------------------------------------------
Name: Sean Casaus
File Name: primenumberTest.py
Specifications: Takes in user input for any positve integer, and displays if the input is prime or not prime.
                    Before closing, the program displays the max, min, sum, count, and average of all inputed numbers greater than 0. 
---------------------------------------------------------------------------------------------------------------------------------------"""
userInput = 1
isPrime = True
allNumbers = [] 
totalCount = 0

#Pupose of these loop is to remain in the program as long as the user does not enter 0.
    #Any negative number will be met with an error message, but remains in loop. 
while userInput != 0:
    userInput = input("Enter a positve integer, or enter 0 to quit: ")

    #This if statement serves the sole purpose of determining if an entered number is prime or not, and including it in the sequence.  
    if userInput >= 1:
        totalCount += 1
        allNumbers.append(userInput)
        if userInput is 1 or userInput is 2 or userInput is 3 or userInput is 5 or userInput is 7:
            isPrime = True
        elif userInput % 2 is 0:
            isPrime = False
        elif userInput % 3 is 0:
            isPrime = False            
        elif userInput % 5 is 0:
            isPrime = False            
        elif userInput % 7 is 0:
            isPrime = False       
        elif userInput % 9 is 0:
            isPrime = False            
        elif userInput % 11 is 0:
            isPrime = False    
        elif userInput % 13 is 0:
            isPrime = False        
        elif userInput % 15 is 0:
            isPrime = False
        elif userInput % 17 is 0:
            isPrime = False
                
        if isPrime is False:
            print "The Number is Not Prime!"
        elif isPrime is True:
            print "The Number is Prime!"

    #Before breaking out of the while loop, a max int, min int, sum, average, and total count will be displayed to user. 
    if userInput is 0:
        allNumbers.sort()
        intMax = str(allNumbers[totalCount -1])
        intMin = str(allNumbers[0])
        sumAllNumbers = 0
        for number in allNumbers:
            sumAllNumbers += number
        average = str(float('%.3g'%(sumAllNumbers)) / totalCount)
        totalCount = str(totalCount)
        sumAllNumbers = str(sumAllNumbers)

        print"The maximum positive number is " + intMax + "."
        print"The minimum positive number is " + intMin + "."
        print"The sum is " + sumAllNumbers + "."
        print"The count of all number(s) is " + totalCount + "."
        print"The average of all number(s) is " + average + "."
        print"Thanks for playing!"

    if userInput < 0:
        print"Invalid Input!"
