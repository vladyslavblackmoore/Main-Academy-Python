'''Write a program, which takes a year as input and returns message if this is a leap year or note. 
   Please handle the exceptions which may arise is a user will enter non-numeric symbols.'''
   
def checkLeap(inputYear):
    if int(inputYear) % 4 == 0:
        return True
    elif int(inputYear) % 100 == 0 and int(inputYear) % 400 == 0:
        return True
    else:
        return False


def inputCheck(inputYeat):
    if inputYear.isdigit():
        if checkLeap(inputYear) is True:
            return True
        else:
            print('Your Year is not leap')
    else:
        print('Enter the number!')
    return False


while True:
    inputYear = input("Enter the year you want to check: ")
    if inputCheck(inputYear) is False:
        continue
    print(f'Your Year: {inputYear} is Leap')
    break
