
# string = 'abcd'
# numberstorepeat = 20

string= input('Enter a string: ')
numberstorepeat= int(input('enter a number: '))

if len(string) >= numberstorepeat:
    print(string[: numberstorepeat])
else:
    string2 = string*numberstorepeat
    string2=string2[: numberstorepeat]
    print(string2)
    print(string2.count(string))