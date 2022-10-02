from PIL import Image
from generateMaze import generateMaze

maze = generateMaze((31, 31))

maze.generate()
x = maze.size[0]
y = maze.size[1]

img = Image.new('RGB', (x, y), (255, 255, 255))
imgpx = img.load()
for i in range(x):
    for j in range(y):
        if maze.maze[(i*y) + j] == 1:
            imgpx[i, j] = (0, 0, 0)

img.resize((x * 100, y * 100), Image.BOX)
img.save('test.png')

