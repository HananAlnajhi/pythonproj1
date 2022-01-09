print("Welcome in our program:\n")
print("Enter 3 persons:\n")
i = 0
count = 3
person =[]
while i < count:
     x=input()
     person.append(x)
     i += 1
print(person)
print("Do you want other persons enter yes or no:\n")
j = input()
while j == "yes":
  x=input()
  person.append(x)
  print("Do you want other persons enter yes or no:\n")
  j=input()
else:
  print("The persons:" , person)
