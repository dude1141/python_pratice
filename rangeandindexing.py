numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 4, 5]

# count=0
for i in range(len(numbers)):
    print("firstloop",numbers[i])
    for j in range(i+1,len(numbers)):
        print("secondloop",numbers[j])
        if( numbers[i]==numbers[j]):
            print(numbers[i])
            
            
characs = "xxyyds"
printed=set()
# count=0
for i in range(len(characs)):
    print("firstloop",characs[i])
    for j in range(i+1,len(characs)):
        print("printed-->i",printed)
        if(characs[i]==characs[j]) and characs[i] not in printed:
            print("characterof-->i",characs[i])
            printed.add(characs[i])
            
            
characs = "aadde"
printed = ""
for i in characs:
    if characs.count(i) > 1 and i not in printed:
        print("printed...>",printed)
        printed=printed+ i
        print("printed...",printed)
print("final",printed)
