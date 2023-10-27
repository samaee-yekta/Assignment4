import random

pc_number = random.randint(0, 50)
count = 0
while True:
    user_number = int(input('Enter a number between 1 to 50: '))
    count+=1

    if user_number == pc_number:
        print('Great!')
        break 
    if user_number < pc_number:
        print('Enter a bigger number!')

    if user_number > pc_number:
        print('Enter a smaller number')

print('The number is: ',pc_number)
print('You guessed in '+ str(count) + ' tries!')