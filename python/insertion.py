#import matplotlib.pyplot as plt  
def insertionsort(arr):
    n=len(arr)
    for i in range(1,len(arr)):
        j=i 
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1] 
            j-=1 
arr=[] 
n=int(input("How many elements??")) 
for i in range(n): 
    arr.append(int(input("Enter %d number:" %i))) 
print("before swapping:",arr) 
insertionsort(arr) 
print("After swapping:",arr) 
x=list(range(1,10000))  
plt.plot(x , [y*y for y in x] ) 
plt.title("Insertion Sort- Time Complexity is O(n\u00b2)") 
plt.xlabel("Input") 
plt.ylabel(" Time")  
plt.show()
