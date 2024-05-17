class point:
    def _init_(self, x, y):
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


points = []
for _ in range(5):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    random_point = Point(x, y)
    points.append(random_point)

points.append(Point(random.randint(-100, 100),
                    random.randint(-100, 100)))

two lines of code
chat gpt (gian pier tonino)

