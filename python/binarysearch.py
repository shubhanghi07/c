array =[1,2,3,4,5,6,7,8,9] 
def binary_search(searchfor,array):
    lowerbound=0 
    upperbound=len(array)-1 
    found=False 
    while found==False and lowerbound<=upperbound: 
        midpoint=(lowerbound+upperbound)//2 
        if array[midpoint]==searchfor: 
            found =True 
            return found 
        elif array[midpoint]<searchfor: 
            lowerbound=midpoint+1 
        else: 
            upperbound=midpoint-1 
    return found 
searchfor=int(input("what are you searching for?")) 
if binary_search(searchfor,array): 
    print ("element found") 
else: 
    print ("element not found")
