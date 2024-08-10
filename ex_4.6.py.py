def computepay(h, r):
    ph = float(h)
    pr = float(r)
    ot_hours = (ph - 40) * (pr * 1.5)
    total_ot_pay = ot_hours + (40 * pr)
    regular_pay = ph * pr
    if float(h) > 40 :
        return total_ot_pay
    else:
        return regular_pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs, rate)
print("Pay", p)