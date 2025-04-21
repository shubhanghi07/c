def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i,end=" ")

        for j in hashTable[i]:
            print("-->",end=" ")
            print(j,end=" ")

        print()

HashTable=[[] for _ in range(10)]

def hashing(keyvalue):
    return keyvalue% len(HashTable)

def insert(HashTable,keyvalue,value):
    hash_key=hashing(keyvalue)
    HashTable[hash_key].append(value)

insert(HashTable,10,'allahabad')
insert(HashTable,25,'mumbai')
insert(HashTable,20,'mathuara')
insert(HashTable,9,'delhi')
insert(HashTable,21,'punjab')
insert(HashTable,21,'noida')
display_hash(HashTable)



