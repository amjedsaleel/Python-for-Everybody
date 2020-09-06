def computepay(h,r):
    if h > 40 :
        normal_pay = h * rate
        over_time = (h - 40.0) * (rate * 0.5)
        pay = normal_pay + over_time
    else:
        pay = h * rate
    return pay


hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
p = computepay(hours,rate)
print("Pay",p)
