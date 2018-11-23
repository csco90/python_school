# import numpy as np
# problem=[10,49,78,10,10,49,23, 100, 55, 55, 23,55]
# problem=np.array(problem)

# numbers=[]
# for i in problem:
#     if i not in numbers:
#         numbers.append(i)

# #print(numbers)

# count=0
# for i in numbers:
#     filter=problem==i

#     if len(problem[filter])>=2:
#         hold=len(problem[filter])//2
#         count+=hold

# print(count)

'''with a non numpy approach'''

ar=[10,20,20,10,10,30,50,10,20]
t_num=9

ar.sort()

numbers=[]
for i in ar:
    if i not in numbers:
        numbers.append(i)

totalCount=0
for i in numbers:
    count = 0
    for j in ar:

        if i==j:
            count+=1

    if count//2>=1:
        totalCount=totalCount+count//2


print(totalCount)




