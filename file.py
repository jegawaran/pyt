name="jegatheeswaran"
f= open('jega.txt','r')
#f.write('hi this is file \n')
#f.write('here we can use11111111111jjjjjjjjegatheeswaran ' + name + ' words')

for line in f:
    splitt = line.split(' ')
    print(splitt[1])
f.close()
