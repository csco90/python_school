
c=[0, 0, 0, 1, 0, 0]
n=len(c)

position=0
jump=0
while position<n-1:

    try:
        if c[position + 2] != 1:
            position = position + 2
            jump = jump + 1
        else:
            position = position + 1
            jump = jump + 1
    except:

        position = position + 1
        jump = jump + 1






print(jump)



