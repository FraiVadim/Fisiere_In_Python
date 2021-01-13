with open('input.txt','r') as f:
    x=f.readline()
with open('output.txt','w') as f:
    f.write(str(int(x)-2))
    f.write('\n')
    f.write(str(int(x)-1))
    f.write('\n')
    f.write(str(x))
    f.write('\n')
    f.write(str(int(x)+1))
    f.write('\n')
    f.write(str(int(x)+2))