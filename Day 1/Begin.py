def twoNumber():

    data = open("input.txt", "r")
    
    list = []

    for line in data.readlines():
        
        line = line.split()
        if line:
            line = [int(i) for i in line]
            list.append(line[0])
    
    for number1 in list:

        for number2 in list:

            if(number1 + number2 == 2020):
                ans = number1 * number2
                break

    print(ans)
    data.close
    
print(twoNumber())