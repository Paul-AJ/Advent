def Slope():

    data = open("input.txt", "r")
    list = []
    width, length = 0, 0

    for line in data.readlines():
        list.append([line.rstrip()])
        width = len(line)-1
        length += 1

    times = (length * 3) // width

    for line in list:
        
        temporary = line[0]
        t = 0
        while (t < times):
            
            line[0] += temporary
            t += 1
    
    ans = 0
    iter = 0
    for l in list:
        
        for line in l:
            
            if(line[iter] == "#"):
                ans+= 1

            iter += 3
            continue

    return "Answer is ", ans

print(Slope()) # 257