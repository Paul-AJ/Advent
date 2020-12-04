def BadPassword():

    data = open("input.txt", "r")
    valid = 0

    for line in data.readlines():
        
        list = line.split(" ")
        list2 = (list[0].split("-"))

        letter = list[1][0]
        min = list2[0]
        max = list2[1]

        counter = 0
        for c in list[2]:
            
            if(c == letter):
                counter += 1

        if(counter >= int(min) and counter <= int(max)):
            valid += 1

    data.close
    print(valid)

print(BadPassword())

