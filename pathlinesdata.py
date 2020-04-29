import math
line1 = [[0,0],[100,0],[200,0],[300,0],[400,0],[500,0],[600,0]]
line9 = []
line2 = []
line3 = []
line4 = []
line5 = []
line6 = []
line7 = []
line8 = []

lin2rat = 0.466 #tan25deg
disrat = 0.906 # cos 25deg
distance = []
for i in line1:
    temp = []
    temp.append(i[0])
    temp.append(round((600-i[0])*lin2rat,3))
    distance.append(round((600-i[0])/disrat,3))
    line2.append(temp)
ini = 25
add = 21.66
ini += add 
for i in distance:
    line3.append([round(600 - i*math.cos(math.radians(ini)),3),round(i*math.sin(math.radians(ini)),3)])

ini += add 
for i in distance:
    line4.append([round(600 - i*math.cos(math.radians(ini)),3),round(i*math.sin(math.radians(ini)),3)])
    
for i in distance:
    line5.append([600,i])

for i in line4:
    line6.append([round(1200 - i[0],3),i[1]])
    
for i in line3:
    line7.append([1200 - i[0],i[1]])

for i in line2:
    line8.append([1200 - i[0],i[1]])
    
for i in line1:
    line9.append([1200 - i[0],i[1]])
    
lindic = {1:line1,2:line2,3:line3,4:line4,5:line5,6:line6,7:line7,8:line8,9:line9}
# print(lindic)
finalcoor = []
for line in range(1,len(lindic)):
    for i in range(len(line1) - 1):
        finalcoor.append([lindic[line][i],lindic[line][i+1],lindic[line+1][i+1],lindic[line+1][i]])
    
temp = []    
for i in range(1,10):
    temp.append(lindic[i][3][1]/(600 -lindic[i][3][0]+1))
    
        
print(finalcoor)
print(temp)
