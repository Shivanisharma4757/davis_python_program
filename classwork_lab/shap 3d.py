# Simple Python Program: shape3d
# Calculate Volume and Surface Area of Cube, Sphere, Cylinder

import math  # Needed for pi

# ----------------------------
# Cube
# ----------------------------
side = float(input("Enter side of the cube: "))
cube_volume = side ** 3
cube_surface = 6 * (side ** 2)
print(f"Cube -> Volume: {cube_volume}, Surface Area: {cube_surface}")

# ----------------------------
# Sphere
# ----------------------------
radius = float(input("Enter radius of the sphere: "))
sphere_volume = (4/3) * math.pi * (radius ** 3)
sphere_surface = 4 * math.pi * (radius ** 2)
print(f"Sphere -> Volume: {sphere_volume:.2f}, Surface Area: {sphere_surface:.2f}")

# ----------------------------
# Cylinder
# ----------------------------
radius = float(input("Enter radius of the cylinder: "))
height = float(input("Enter height of the cylinder: "))
cylinder_volume = math.pi * (radius ** 2) * height
cylinder_surface = 2 * math.pi * radius * (radius + height)
print(f"Cylinder -> Volume: {cylinder_volume:.2f}, Surface Area: {cylinder_surface:.2f}")

output

Enter side of the cube: 3
Cube -> Volume: 27.0, Surface Area: 54.0
Enter radius of the sphere: 2
Sphere -> Volume: 33.51, Surface Area: 50.27
Enter radius of the cylinder: 2
Enter height of the cylinder: 5
Cylinder -> Volume: 62.83, Surface Area: 87.96
