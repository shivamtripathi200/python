# Movie tickets are priced based on age:
# $12 for adults(18 and over),$8 for children
# .Everyone gets a 2$ discout on wednesday

day = input("whats the day today: ")
age = int(input("whats your age: "))
price = 12 if age >=18 else 8
if day.upper() == "WEDNESDAY":
    price-=2
    print("Congrats you have a 2$ discount")


print("Ticket price for you is $",price)