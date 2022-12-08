start = int(input())
end = int(input())
for i in range(1,i+1):
    if i > 1:
        for j in range(1,i):
            if(i%j==0):
                break
            else:
                print(i)
             
