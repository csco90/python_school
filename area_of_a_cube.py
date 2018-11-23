''' you can calculate the surface area of a cube if you know the 
length of an edge.
A_surface=6*lenght_edge**2
'''

#get the length of one of the cube's side
lenght_edge=int(round(eval(input('Enter the length of an edge: '))))

# calculate the Surface Area
A_surface=6*lenght_edge**2

#displaying the result
print(A_surface)