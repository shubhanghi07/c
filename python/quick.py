#import matplotlib.pyplot as plt 
def partition(arr,low,high): 
    p=arr[low] 
    i=low+1 
    j=high 
    while True: 
        while i<=j and arr[i]<=p: 
            i+=1 
        while i<=j and arr[j]>=p: 
            j-=1 
        if i<=j: 
            arr[i],arr[j] = arr[j],arr[i] 
        else: 
            break 
    arr[low],arr[j] = arr[j],arr[low] 
    return j 
def quickSort(arr,low,high): 
    if low < high: 
        pivot = partition(arr,low,high) 
        quickSort(arr, low, pivot-1) 
        quickSort(arr, pivot+1, high) 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
x=list(range(1,10000)) 
plt.plot(x , [y*y for y in x] ) 
plt.title("Quick Sort- Time Complexity is O(n\u00b2)")
plt.xlabel("Input") 
plt.ylabel(" Time") 
plt.show()
