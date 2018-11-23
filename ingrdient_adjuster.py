"""This program will ask the user how many cookies she/he 
are going to make and the adjust and print the amount of ingredients 
the user will need to prepare the recipe
Based on this recipe to create 48 cookies:
1.5 Cups of sugar
1 cup of butter
2.75 cups of flour
"""

#ask the amount of cookies:
cookies=eval(input("How many cookies would you like to prepare? "))

butter=cookies/48
sugar=1.5*cookies/48
flour=2.75*cookies/48

#calculating the amount of ingredients
print("You'll need:\n" + str(format(1.5*cookies/48,'.1f')) + " Cups of sugar.\n" + str(format(cookies/48,'.1f'))\
	+ " Cups of butter.\n" + str(format(2.75*cookies/48,'.1f')) + " Cups of flour.")