print("Welcome In Our Prog")
total =0
while total<=50:
    x=input("Enter Number:")
    total=total+int(x)
    if(total>50):
        print("The total is greater than 50")
        break
    print("The total is:",total)