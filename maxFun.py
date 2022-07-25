def myMaxFun(list):
    for n in range(0, len(list)):
     list[n] = int(list[n])

    max = 0
    for x in list:
     if x>max:
        max = x
     else:
        max = max    

    print(max) 

myMaxFun(["10","20","5"])    
