import random
word_list =[
    {"word": "Yemen", "question": "Country?"},
    {"word": "Forg", "question": "Country?"},
    {"word": "yes", "question": "Anser?"},
    {"word": "July", "question": "The seventh month of the year"},
    {"word": "Python", "question": "A programming language"},
    {"word": "ِAlgeria", "question": "The biggest country in Africa"},
    {"word": "Happy", "question": "Opposite of sad"},
    {"word": "Manila", "question": "The capital of the Philippines"},
    {"word": "Tigris", "question": "ِA river in Iraq"},
    {"word": "Joe Biden", "question": "The president of America "},
    {"word": "Abdel Halim Hafez", "question": "An Egyptian singer"},
    {"word": " censorious", "question": "The synonym of critical"},
    {"word": "S400", "question": "Air missile system"},
    {"word": "orang", "quest": "what is orang color?"},
    {"word": "red", "quest": "what is appale color?"},
    {"word": "yallow", "quest": "what is banana color?"},
    {"word": "rose", "quest": "what is Strawberry color?"},
    {"word": "green", "quest": "what is watermelon color?"},
    {"word": "black", "quest": "what is Grape color?"},
    {"word": "blue", "quest": "what is Cranberries color?"},
    {"word": "white", "quest": "what is fig color?"},
    {"word": "browen", "quest": "what is Kiwi color?"},
    {"word": "darkgreen", "quest": "what is avocado color?"},
    {"word": "songs", "question": "which You listen everyday?"},
    {"word": "nliy", "question": "Her most important work is a movie and men.?"}
]

newlist=[]
newlist1=[]
for i in word_list:
    for j in list(i.values())[0]:
        print("", end=" ")
    newlist.append(list(i.values())[0])
for i in newlist:
    print(i,"", end="")

words = random.choice(newlist)

#print(words)
"""for y in range(6):
        print("\n")
        for x in random.choice(newlist[random.randint(0,7)]):
            print(x, end=" ")
            for z in random.choice(newlist[random.randint(0,7)]):
                print(z, end=" ")
                for z in random.choice(newlist[random.randint(0, 7)]):
                    print(z, end=" ")
                    for z in random.choice(newlist[random.randint(0, 7)]):
                        print(z, end=" ")
                        for z in random.choice(newlist[random.randint(0, 7)]):
                            print(z, end=" ")
                            for z in random.choice(newlist[random.randint(0, 7)]):
                                print(z, end=" ")"""

count = 0
for y in range(6):
    print("\n")
    wordcol = random.choice(newlist)
    if(len(wordcol)<=6):
        if (count <= len(wordcol)):
            for x in wordcol:
                wordRn = random.choice(newlist[random.randint(0, 7)])
                print(wordRn," ", end="")
                count += 1

            else:
                dec = 6 - count
                for x in range(dec):
                    print("-"," " ,end="")
                count = 0
    else: continue