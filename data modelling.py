class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = point(2, 3)
b = point(7, 9)
c = point(10,11)

print(f"a=({a.x}, {a.y})")
print(f"b=({b.x}, {b.y})")
print(f"c=({c.x}, {c.y})")

import random

def generate_random_points(num_points):
    points = []
    for _ in range(num_points):
        x = random.randint(-10, 10)  # Adjust range as needed
        y = random.randint(-10, 10)  # Adjust range as needed
        points.append((x, y))
    return points

num_points = 5
random_points = generate_random_points(num_points)
print("Random points:")
for point in random_points:
    print(point)

colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(colors)
                     )
    )

print(colored_points)
# main attributes of 2d points needs to have x and y, call innit everytime
# magic method starts with double underscore
