# Claudio Castillo
size=-1
average=-1
days=-1


size=int(input('Starting number of organisms: '))
while size<2:
   print("The starting number of organisms must be at least 2.")
   size = int(input('Starting number of organisms: '))

# Get a valid value for the average daily
# increase from the user.
# Do not accept negative values for the

average=float(input('Average daily increase: '))

while average<=0:
   print('Average daily increase must be a positive number: ')
   average = float(input('Average daily increase: '))

# Get a valid value for the number of days
# to multiply from the user.


while days<1:
   days = int(input('Number of days to multiply: '))
   print('Number of days must be at least 1: ')



# Determine if the average daily increase was
# input as a whole number; if so, divide by
# 100 to format the value as a percentage.
if average>1:
   average=average*.01

# Calculate and print amount of increase each day.
print('Day Approximate\t\t Population')
print('-----------------------------------')
increment=0
population=size
# Apply the increase after the first day.
for day in range(days):
   population=population+increment
   print((day + 1), '\t\t\t', population)
   increment=population*average