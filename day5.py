lines = open("k.txt").read().splitlines()
w = 1000
floormap = [[0]*w for i in range(w)]

def markFloormap(p1,p2):
    if p1[0] == p2[0]:
        larger = max(int(p2[1]),int(p1[1]))
        smaller = min(int(p2[1]),int(p1[1]))
        for i in range(int(smaller),int(larger)+1):
            floormap[int(p1[0])][i] += 1
            continue
    elif p1[1] == p2[1]:
        larger = max(int(p2[0]),int(p1[0]))
        smaller = min(int(p2[0]),int(p1[0]))
        for i in range(int(smaller),int(larger)+1):
            
            floormap[i][int(p1[1])] += 1
            continue
    else:
        x1 = int(p1[0])
        y1 = int(p1[1])
        x2 = int(p2[0])
        y2 = int(p2[1])
        if x2>x1:
            xStep = 1
        else:
            xStep = -1
        if y2>y1:
            yStep=1
        else:
            yStep = -1
        n = 0
        for i in range(x1,x2+xStep,xStep):
            floormap[i][y1+(yStep*n)] += 1
            n += 1

for line in lines:
    points = [p.split(',') for p in line.split(' -> ')]
    #if points[0][0] == points[1][0] or points[0][1] == points[1][1]:
    markFloormap(points[0],points[1])

            
count = 0
for i in range(0,w):
    for j in range(0,w):
        if floormap[i][j] > 1:
            count += 1

print(count)