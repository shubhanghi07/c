import time
import matplotlib.pyplot as plt
def selectionsort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp

a=[]
n=int(input("how may terms:"))
for i in range(n):
    a.append(int(input("enter %d number:"%i)))
selectionsort(a)
print(a)
x= list(range(1,10000)) 
plt.plot(x,[y*y for y in x]) 
plt.title("selection sort time complexity is O(n\u00b2)") 
plt.xlabel("input") 
plt.ylabel("time") 
plt.show()

