with open('globulet.txt ','r') as f:
    a=f.readline()
r=int(a)+2
ar=int(a)+int(r)
b=int(ar)-2
t=int(a)+b+r
with open('bradul.txt','w') as f:
    f.write(str(t))