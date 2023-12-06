per_age=int(input("Enter age to get ticket price"))
if per_age==0 and per_age<=3:
    print("free")
elif per_age==4 and per_age<=12:
    print("ticket price is $10")
elif per_age==13 and per_age<=17:
    print("ticket price is $15")
else:
    print("ticket price is $20")           