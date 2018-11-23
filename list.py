

days_of_the_week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']
daily_sales=[0,0,0,0,0,0,0]

print(days_of_the_week[0])
print(days_of_the_week[1])
print("")

# for i in range(len(days_of_the_week)):
#     print(days_of_the_week[i])
# print('')
#
# for i in days_of_the_week:
#     print(i)


for i in range(len(daily_sales)):
    daily_sales[i]=int(input('Enter the sales for: ' + days_of_the_week[i] + ': '))

total=0


count=0
for sale in daily_sales:
    count+=1
    total+=sale
average=total/count
print(total, average)

for i in range(len(days_of_the_week)):
    print('The sales for %10s is %5d' %(days_of_the_week[i], daily_sales[i]))




