quiz= input(("how old is mungo man?"))
if quiz=="about 50000 years old":
    print("correct")
else :
    print("wrong") 
    print("try again")

#task2
costprice=int (input("how much did you spend to buy the item?"))
sellprice=int(input("how much did yopu sell it for?"))
if sellprice>costprice:
    print("you made a profit")
    money=sellprice-costprice
    print("you made a profit of ",money)
else:
    print("you didn't make a profit")
    moneylos=costprice-sellprice
    print("you made a lose of ",moneylos)

