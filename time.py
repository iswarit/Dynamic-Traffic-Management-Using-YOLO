lanes= {}
with open("log.txt") as file:
    for line in file:
        (key, val) = line.split()
        lanes[str(key)] = val
        
for keyVal in lanes:
    print(keyVal, '=', lanes[keyVal], 'vehicles')
   

vals=list(lanes.values())


if(int(vals[0])>10 and int(vals[1])>23 and int(vals[2])>17 and int(vals[3])>10 ):
    print("Default time Activated")
    print("Time for lane 1 is 30 Seconds")
    print("Time for lane 2 is 30 Seconds")
    print("Time for lane 3 is 30 Seconds")
    print("Time for lane 4 is 30 Seconds")

if(int(vals[0])==10 and int(vals[1])==23 and int(vals[2])==17 and int(vals[3])==10 ):
    print("New time Activated")
    print("Time for lane 1 is 30 Seconds")
    print("Time for lane 2 is 35 Seconds")
    print("Time for lane 3 is 25 Seconds")
    print("Time for lane 4 is 30 Seconds")



if(len(lanes)>4):
    open("log.txt", "w").close()





 