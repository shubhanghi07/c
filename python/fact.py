def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num=4
if num<0:
    print("fact not for nagative number")
elif num==0:
    print("the fact of 0 is 1")
else:
    print("factorial of",num,"is",recur_factorial(num))
    
