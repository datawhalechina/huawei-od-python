from queue import Queue
inputList=[]
while True:
    try:
        line=input()
        inputList.append(line)
    except EOFError:
        break
rows=len(inputList)
cols=len(inputList[0].split())
girdCopy=[[None]*cols for _ in range(rows)]
noNums=0

q=Queue()
for i in range(rows):
    strings=inputList[i].split()
    girdCopy[i]=strings[:cols]
    noNums+=strings.count("NO")
    for j in range(cols):
        if girdCopy[i][j]=="YES":
            q.put((i,j))
day=0
while not q.empty() and noNums !=0:
    size=q.qsize()
    for _ in range(size):
        i,j=q.get()
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        for dir in directions:
            newrow=i+dir[0]
            newcol=j+dir[1]
            if 0<=newrow<rows and 0<=newcol <cols and girdCopy[newrow][newcol]=="NO":
                girdCopy[newrow][newcol]="YES"
                noNums=-1
                q.put(newrow,newcol)
    day+=1


print(day) if noNums==0 else print(-1)