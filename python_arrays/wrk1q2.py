def findname(names):
    max = len(names)
    name = str(input("Enter name"))
    for i in range(0,max):
        if names[i] == name:
            found = True
            recordnum = i
        #endif
    #next i
    if found == True:
        print(recordnum + 1)
    else:
        print("name not found")
    #endif
    return
#end procedure