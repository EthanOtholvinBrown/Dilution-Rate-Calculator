# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:35:56 2020

@author: Ethan Brown
"""
import math #brings in module for calculating square root
import random #brings in the madule which provides a random number
quitValue = "quit" #sets up a variable for all functions to recognize the need 
                    #to quit
#Create variables for range of s0
S0_LOW = 25
S0_HIGH = 75
#create variables for range of umax
UMAX_LOW = 0.2
UMAX_HIGH = 0.7
#create variables for range of random
RAND_LOW = 2
RAND_HIGH = 7
#create variable for s0 mod check
MOD_VAL = 5
#create variables for acceptable parameter range
ACCEPTABLE_LOW = 0.35
ACCEPTABLE_HIGH = 0.45
#start the main function
def main():
    #create variables for the user exit decisions
    userChoice_YES = 'y'
    userChoice_NO = 'n'
    userChoice = userChoice_NO    
    print("This program will calculate the maximum dilution rate in a CSTR.")
    while (userChoice == userChoice_NO):
        print("WARNING! This program will check if values are within range after all",
              "values are entered!")        
        #prompt the user for an s0 value
        s0 = int(input("Enter an 'S0' value that is divisible by 5 [25-75]: "))    
        #prompt the user for a Umax value
        uMax = float(input("Enter a 'UMax'[0.2-0.7]: "))
        #enter user values into the function for calculating dilution
        resultValue = CalcDilution(s0,uMax)
        #only proceed if there is no quit value present
        if(resultValue[0] != quitValue): 
            #display result of calculation and information utilized for 
            #calculation
            print("The maximum dilution is: ",format(resultValue[0],'0.4f'),
                                                     " per hour")
            print("Entered S0: ",s0)
            print("Entered Umax: ",uMax)
            print("Random value used: ",resultValue[1])  
            #check if final value is within parameters
            finalCheck = withinParameters(resultValue[0])
            print(finalCheck)#output result of parameters check
            #decide whether to end program or run it again
            userChoice = str(input("End program? [y,n]: "))
            if (userChoice == userChoice_YES):
                print("Goodbye! Thank you for using this program!")
            else:
                #if neither 'y' or 'n' is chosen, prompt the user again
                while(userChoice != userChoice_YES and userChoice != userChoice_NO):
                    print("That wasn't a valid option.")
                    userChoice = str(input("End program? [y,n]: "))
                    #display exit message if 'y' is chosen
                    if (userChoice == userChoice_YES):
                        print("Goodbye! Thank you for using this program!")                    
        #if a quit value is present, end program and display where 
        #the issue was
        else:
            #identify which value is incorrect
            failCheck = CheckValues(s0,uMax) 
            if (failCheck[0] == quitValue and failCheck[1] == quitValue):
                print("Both values are invalid. Exiting program.")
                print("Goodbye! Thank you for using this program!")
                userChoice = userChoice_YES                
            else: 
                if(failCheck[0] == quitValue):
                    print(s0," Is not an acceptable value for s0. Exiting program.")
                    print("Goodbye! Thank you for using this program!")
                    userChoice = userChoice_YES
                if(failCheck[1] == quitValue):
                    print(uMax
                          ," Is not an acceptable value for Umax. Exiting program.")
                    print("Goodbye! Thank you for using this program!")
                    userChoice = userChoice_YES  
#function for checking if user inputted values are within range
def CheckValues(val1,val2):
    checkedVal1 = val1%MOD_VAL#check if s0 value is divisible by 5
    #check neither is within range, return a quit value if not
    if ((val1 < S0_LOW or val1 > S0_HIGH) and (val2 < UMAX_LOW or val2 > UMAX_HIGH)):
        val1 = quitValue
        val2 = quitValue        
        return val1,val2    
    else:
        #check if s0 is within range, return a quit value if it's not
        if(val1 < S0_LOW or val1 > S0_HIGH):
            val1 = quitValue
            return val1,val2
        #check if umax is within range, return a quit value if it's not
        elif(val2 < UMAX_LOW or val2 > UMAX_HIGH):
            val2 = quitValue
            return val1,val2
        #confirm if s0 is divisible by 5,  return a quit value if not
        else:
            if(checkedVal1 != 0):
                print("S0 is not divisible by 5.")
                return quitValue,""
            return val1, val2
#create the function for calculating the dilution
def CalcDilution(userS0,userUmax):
    #call checkValues function to confirm values are in range
    valuesForCalc = CheckValues(userS0,userUmax)
    #create a random number for calculations
    myRando = random.randint(RAND_LOW,RAND_HIGH)
    #if either user entered values have a 'quit' value, tell the main function
    if(valuesForCalc[0] == quitValue or valuesForCalc[1] == quitValue):
        return quitValue,""        
    else:
        #if there are no quit values, perform the calculation and 
        #return the result as well as the random number value
        dilutionMax = userUmax*(1-(math.sqrt(myRando/(myRando+userS0))))
        return dilutionMax,myRando
#create a function for checking if dilution rate is within acceptable 
#parameters
def withinParameters(givenDilution):
    goodOrNot = "Kinetic parameters are acceptable."
    if(givenDilution > ACCEPTABLE_LOW and givenDilution < ACCEPTABLE_HIGH):
        return goodOrNot #if value is in range, tell the main function
    else:
        goodOrNot = "Kinetic parameters are not acceptable."
        return goodOrNot #if value is not in range, tell the main function
main() #run the main function