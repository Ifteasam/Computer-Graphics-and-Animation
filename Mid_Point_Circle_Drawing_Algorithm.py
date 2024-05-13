from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

def draw_circle(center_h, center_k, radius):
    # Set starting values
    x = 0
    y = radius
    d = 1 - radius

    # Create empty lists to hold circle points
    circle_points = []

    print("Intermediate Points : ")
    while x <= y:
        # Add points to the circle_points list (8 symmetric)
        circle_points.append((x + center_h, y + center_k))
        circle_points.append((-x + center_h, y + center_k))
        circle_points.append((x + center_h, -y + center_k))
        circle_points.append((-x + center_h, -y + center_k))
        circle_points.append((y + center_h, x + center_k))
        circle_points.append((-y + center_h, x + center_k))
        circle_points.append((y + center_h, -x + center_k))
        circle_points.append((-y + center_h, -x + center_k))
        print(x,'\t',y)
        # Check if midpoint is inside or outside the circle and update values accordingly
        if d < 0:
            d = d + 2 * x + 1
        else:
            d = d - 2 * y + 2 * x + 1
            y = y - 1
        x = x + 1

    # Plot the circle points
    plt.scatter(*zip(*circle_points), s=20, color='red')
    plt.xlabel('X Cordinates')
    plt.ylabel('Y Cordinates')
    plt.title("Mid Points Circle Drawing Algorithm")
    plt.grid(True)
    plt.legend()
    plt.show()

# User Input for the radius of the circle
radius = int(input("Enter the radius of the circle: "))

# Call the draw_circle function with center_h and center_k as 0, and the user input radius
draw_circle(0, 0, radius)
