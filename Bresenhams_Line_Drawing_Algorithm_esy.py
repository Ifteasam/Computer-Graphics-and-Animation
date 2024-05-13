from matplotlib import pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    k = dx - dy
    x, y = x1, y1
    points = []
    
    print("Xi\tYi")
    while True:
        points.append((x, y))
        print(x,'\t',y)
        if x == x2 and y == y2:
            break
        p = 2 * k
        if p > -dy:
            k -= dy
            x += sx
        if p < dx:
            k += dx
            y += sy
    return points

x1 = int(input("Enter the x-coordinate of the starting point: "))
y1 = int(input("Enter the y-coordinate of the starting point: "))
x2 = int(input("Enter the x-coordinate of the ending point: "))
y2 = int(input("Enter the y-coordinate of the ending point: "))
    
points = bresenham_line(x1, y1, x2, y2)

#plot the poitns
xcoordinates, ycoordinates = zip(*points)
plt.plot(xcoordinates, ycoordinates, color='red', marker='o', linewidth=2)
plt.xlabel('X Cordinates')
plt.ylabel('Y Cordinates')
plt.title("Bresenham's Line Drawing Algorithm")
plt.grid(True)
plt.legend()
plt.show()