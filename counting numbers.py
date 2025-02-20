#count the nom"s which are divisible by 3 and 5 from 1 to 100
count=0 #defining count number
for i in range(1,101): #setting a numbers
    if(i%3==0 and i%5==0): #setting down condtons
        count=count+1 #adding count values
        print(count) #print counted numbers