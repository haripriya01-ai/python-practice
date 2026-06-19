a=int(input("Enter a number between 1 to 10 :"))

match a :
    case 1:
        print("you won 10 rupees")
    case 2:
        print("you won 100 rupees") 
    case 3:
        print("you won 1000 rupees")       
    case _:
        print("Better luck nesst time")    
