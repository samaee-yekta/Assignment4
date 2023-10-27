import random

a = "y"
while a == "y":
      dice = random.randint(1,6)
      if dice == 6:
            print(dice) 
            a = random.randint(1,6)
            print ("Your first bonus is: ",a)
            b = random.randint(1,6)
            print("Your secound bonus is: ",b)
      else:
            print(dice)

      a = input("Press y to continue or n to end: ")
      if a == "n":
            break