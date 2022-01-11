print("Chose number of people the user wants to invite to a party:")
ch = input()
if(int(ch)<10):
    print("Enter Name of persons:")
    i=0
    person = []
    while i < int(ch):
        x = input()
        person.append(x)
        print(person[i], "has been invited")
        i += 1
    print(person, "has been invited")
elif(int(ch)>=10):
    print("Too many people")


