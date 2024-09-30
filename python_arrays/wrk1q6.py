def parksACar(park,reg):
    vald = False
    while vald == False:
    
        row = int(input("enter the car park row you are parking in: "))
        bay = int(input("enter the bay within the row the car is parking in"))
        if (row<1 or row>10) or (bay<1 or bay>6):
            print("Invalid parking space enter again: ")
        else:
            vald = True
        #emdif
    #endwhile
    if park[row-1][bay-1] != "empty":
        print("this is not an empty bay")
    else:
        park[row-1][bay-1] = reg
    #endif
    return park
#endfunction

def intitialise(grid):
    grid = [["empty" for j in range(6)] for i in range(10)]
    return grid
#endfunction




park = []
park = intitialise(park)
print("where do you want to park you car? ")
reg = str(input("enter registration: "))
park = parksACar(park,reg)
print(park)