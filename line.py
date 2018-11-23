
infile=open('philosophers.txt')

line1=infile.readline()
line2=infile.readline()
line3=infile.readline()

infile.close()


print(line1)
print(line2)
print(line3)

# the following loop reproduces the same output
print(len(line3)*"-")
infile=open('philosophers.txt')
for line in (list(infile)):
    print(line)