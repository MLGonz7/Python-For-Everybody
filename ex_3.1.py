#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per 
#hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking or bad user data.



hours = input("Enter Hours:")
rate = input("Pay Per Hour:")
regular_pay = float(hours) * float(rate)
ot_worked = float(hours) - 40
ot_pay = float(rate) * 1.5
total_ot_pay = (ot_worked * ot_pay) + (40 * float(rate))


if float(hours) > 40:
    ot_worked * ot_pay
    print("Pay:", total_ot_pay)
else:
    print("Pay:", regular_pay)
