def TowerOfHanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk one from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1,auxiliary,destination,source)
n=3
TowerOfHanoi(n,'A','B','C')
