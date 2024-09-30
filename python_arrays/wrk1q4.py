total = [0,0,0,0]
for quarter in range(0,4):
    for outlet in range(0,4):
        total[quarter] = total[quarter]+outletSales[quarter,outlet]
    #next outlet
#next quarter

for i in range(0,4):
    print("total for qurater",(i+1),"is",total[i])
#next i