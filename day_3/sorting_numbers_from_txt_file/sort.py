i = open("input.txt", 'r')
Lst = i.read().split()
Lst.sort()
for line in  Lst:
    print(line)
    with open('result.txt', 'w') as f:
        for line in Lst:
            Lst.sort()
            f.write(line)



 

