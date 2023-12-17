"_________________________________Password Generator____________________________________________"
"_______________________CodSoft Internship December A19 Batch______________________________________"
"______________________Code written and submitted by Avinash Gupta____________________________________"
import random
charDict = {
    "Numbers":[0,1,2,3,4,5,6,7,8,9],
    "Symbols":["!","@","#","%","&"],
    "Lowercase":["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    "Uppercase":["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    }

def generatePass(length):
    
    stringPass = ""
    for x in range(length):
        charName = random.choice(list(charDict.keys()))
        char = random.choice(charDict[charName])
        stringPass+=str(char)

    return stringPass

print("______________________Welcome to Password Generator..________________________________")
while True:
    print("")
    userInput = int(input("Enter the Number of Characters you want to have in your Password:  "))
    print("Your Password is: "+generatePass(userInput))
    print("==========================")
    userInput = input("Do you want to run the program again?(y/n): ")
    if userInput=="y":
        continue
    else:
        print("Thank You. Visit again!")
        break
