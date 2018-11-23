
import random

def main():
    number_list=[0,0,0,0,0,0,0]

    for i in range(len(number_list)):
        number_list[i]=random.randint(0,9)

    for i in range(len(number_list)):
        if i!=len(number_list)-1:
            print(number_list[i],end='-')
        else:
            print(number_list[i], end='')




main()