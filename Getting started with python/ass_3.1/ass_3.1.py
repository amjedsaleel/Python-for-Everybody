hrs = input("Enter Hours:")
h = float(hrs)

srate = input("Enter rate")
rate = float(srate)

if h > 40 :
    normal_pay = h * rate
    over_time = (h - 40.0) * (rate * 0.5)
    pay = normal_pay + over_time
else:
    pay = h * rate
print('Pay:', pay)
