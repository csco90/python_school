
data=input ('Enter a number between 0 - 100: ')

print('isdigit: You entered: ', data)


if data.lstrip('-').isdigit():
    print('Yes digit')
    digitInput=True
    print(digitInput)
    if 0<=int(data)<=100:
        print('Between the range')
    else:
        print('Out of the range')

else:
    print('Not digit')
    digitInput=False
    print(digitInpput)

