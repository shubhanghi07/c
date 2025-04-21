import time 
import matplotlib.pyplot as plt  
def linearsearch(a, key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i;
        return -1 
a = [13,24,35,46,57,68,79] 
print("the array elements are:",a) 
key = int(input("enter the key element to search:")) 
result = linearsearch(a,key) 
if result == -1:
    print("Search UnSuccessful") 
else:
    print("Search Successful key found at %d location:" %result) 
end=time.time() 
x= list(range(1,10000)) 
plt.plot(x,[y for y in x]) 
plt.title("Linear Search- Time Complexity is O(n) ") 
plt.xlabel("Input") 
plt.ylabel("Time") 
plt.show()
