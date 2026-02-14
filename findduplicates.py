numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 4, 5]

# count=0
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if( numbers[i]==numbers[j]):
            print(numbers[i])
            
            
characs = "xxxxyyyydddeeeef"
printed=set() #Keep track of unique items already seen and prevent duplicates
# count=0
for i in range(len(characs)):
    for j in range(i+1,len(characs)):
        if(characs[i]==characs[j]) and characs[i] not in printed:
            print(characs[i])
            printed.add(characs[i])
