
def grad(x):
    return 2*x

def upgradeV(x,alpha):
    return x-alpha*grad(x)

alpha=0.001
x0=10
x1=upgradeV(x0,alpha)
diff=x0-x1
count=1
incSign=True

while abs(diff)>1e-5:
    x1 = upgradeV(x0, alpha)
    diff = x0 - x1
    if incSign:
        alpha*=1.5
    else:
        alpha*=0.67
    print(count,'th iteration:','alpha',alpha,',',diff)
    x0 = x1
    count+=1

