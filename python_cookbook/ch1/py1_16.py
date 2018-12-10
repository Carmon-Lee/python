mylist=[1,4,-5,-10,6,33,-9]

a=[n for n in mylist if n>0]
b=[n for n in mylist if n<0]

pos=(n for n in mylist if n>0)
print(a,b)

for n in pos:
    print(n)

values=['1','2','-3','-','4','N/A','5']

def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False
ivalues=list(filter(is_int,values))
print(ivalues)