#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print 
#out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and 
#put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.



largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None :
        largest = number
    elif number > largest :
        largest = number
    if smallest is None :
        smallest = number
    elif number < smallest :
        smallest = number
    
print("Maximum is", largest)
print("Minimum is", smallest)
