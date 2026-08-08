Weather = (1,0,0,0,1,1,0)
sunny = 0 
rainy = 0 
for i in range (0,7):
    if(Weather[i]==0):
        rainy+=1
    else:
        rainy +=1
if (sunny>rainy):
    print("Good weather")
else:
    print("Bad weather")
