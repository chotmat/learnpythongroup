def topbot(n,up):
    i = 0
    numbers = []
    while i < n:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + up
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    
    print("The numbers: ")
   
    for num in numbers:
        print(num)

topbot(5,1)
topbot(3,2)

