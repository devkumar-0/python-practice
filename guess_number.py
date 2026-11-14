from random import *
secret_nu = randint(1,1000)
count = 0
guess = int(input("Give your guessed values: "))
dif = abs(secret_nu - guess)
dif1 = dif
for x in range(0,1):
    if dif == 0:
        print("Correctly guessed")
        break
    else:
        print("wrong guess")
        count = count+1

    ans = input("Want to try more: (Yes(y) OR No(n)) ")
    while ans in ("Yes", "yes", "y"):
            guess = int(input("Give your guessed values: "))
            dif = abs(secret_nu - guess)
            if dif == 0:
                print("Correctly guessed")
                print("Total guessed values: ")
                break
            else:
                if dif>dif1:
                    print("You moved more further than your best guess ")
                elif (dif==dif1):
                    print("your previous guess is same as this one")
                else:
                    print("this guess is more closure")
                    dif1 = dif
            ans = input("Want to try more: (Yes/No) ")
            count+=1
    else:
            print("secret_number:", secret_nu)
        
            
        
       
        
