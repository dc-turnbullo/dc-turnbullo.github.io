    
def quartercalc(outlet1Sales,outlet2Sales,Outlet3sales):
    for i in range(0,4):
        quarter = outlet1Sales[i]+outlet2Sales[i] + outlet3sales[i]
        print("total for quarter", i, "is", quarter)
    #next i
#end procedure