import random
from PIL import Image

x = 31
y = 31
maze = [0 for i in range(x*y)]

def printMaze(maze, x, y):
    for i in range(x):
        for j in range(y):
            print(maze[(j*x) + i], end="")
        print()

def WallMaze(maze, x, y):
    for i in range(x*y):
        maze[i] = 1

def EdgeWall(maze, x, y):
    for i in range(x):
        maze[i] = 1
        maze[(y-1)*x + i] = 1
    for i in range(y):
        maze[i*x] = 1
        maze[i*x + (x-1)] = 1

def generate(maze, x, y):
    random.seed()
    WallMaze(maze, x, y)
    passages = []

    xr = random.randrange(1, x-1, 2)
    yr = random.randrange(1, y-1, 2)
    initialPassage = [yr, xr, yr, xr]
    passages.append(initialPassage)
    while len(passages) > 0:
        p = passages.pop(random.randint(0, len(passages)-1))
        yr = p[2]
        xr = p[3]

        if(maze[(yr*x) + xr] == 1):
            maze[(p[0]*x) + p[1]] = 0
            maze[(yr * x) + xr] = 0

            if yr >= 2 and maze[((yr-2)*x) + xr] == 1:
                newPassage = [yr - 1, xr, yr - 2, xr]
                passages.append(newPassage)

            if xr >= 2 and maze[(yr*x) + (xr-2)] == 1:
                newPassage = [yr, xr-1, yr, xr - 2]
                passages.append(newPassage)

            if yr < y - 2 and maze[((yr+2)*x) + xr] == 1:
                newPassage = [yr + 1, xr, yr + 2, xr]
                passages.append(newPassage)

            if xr < x - 2 and maze[(yr * x) + (xr + 2)] == 1:
                newPassage = [yr, xr + 1, yr, xr + 2]
                passages.append(newPassage)

    EdgeWall(maze, x, y)
    passages.clear()

generate(maze, x, y)
#printMaze(maze, x, y)

img = Image.new('RGB', (x, y), (255, 255, 255))
imgpx = img.load()
for i in range(x):
    for j in range(y):
        if maze[(j * x) + i] == 1:
            imgpx[i, j] = (0, 0, 0)

img.resize((x * 100, y * 100), Image.BOX)
img.save('test.png')