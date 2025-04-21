import time 
import matplotlib.pyplot as plt 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] 
arr = [14, 34, 25, 12, 22, 11, 90] 
bubbleSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)):
    print ("%d" %arr[i]) 
x= list(range(1,10000)) 
plt.plot(x,[y*y for y in x]) 
plt.title("bubble sort time complexity is O(n\u00b2)") 
plt.xlabel("input") 
plt.ylabel("time") 
plt.show()
