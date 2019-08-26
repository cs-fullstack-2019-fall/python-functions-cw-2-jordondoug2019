

def calculator():
    numInput= int(input("enter a number "))
    numInput2=int(input("Enter a 2nd number "))
    # !! : "Use the function to get two numbers from the user, then pass the two numbers to a function". your math actions should be in a different funciton 
    print(numInput+numInput2)
    print(numInput-numInput2)
    print(numInput*numInput2)
    print(numInput/numInput2)

def number():
    calculator()

number()