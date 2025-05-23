#import matplotlib.pyplot as plt 
def merge(left, right): 
    if not len(left) or not len(right): 
        return left or right 
    result = [] 
    i, j = 0, 0 
    while (len(result) < len(left) + len(right)): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i+= 1 
        else: 
            result.append(right[j]) 
            j+= 1 
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break 
    return result 
def mergesort(list):
    if len(list) < 2: 
        return list 
    middle = int(len(list)/2) 
    left = mergesort(list[:middle]) 
    right = mergesort(list[middle:]) 
    return merge(left, right) 
seq = [12, 11, 13, 5, 6, 7] 
print("Given array is") 
print(seq) 
print("\n") 
print("Sorted array is") 
print(mergesort(seq)) 
x=list(range(1,10000)) 
plt.plot(x , [y*y for y in x] ) 
plt.title("Merge Sort- Time Complexity ")
plt.xlabel("Input") 
plt.ylabel("Time") 
plt.show()
