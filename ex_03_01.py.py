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