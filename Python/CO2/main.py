import graphics.rectangle as rect
print("Rectangle Area:", rect.area(10, 5))
print("Rectangle Perimeter:", rect.perimeter(10, 5))

from graphics.circle import area, perimeter
print("\nCircle Area:", area(7))
print("Circle Perimeter:", perimeter(7))

from graphics.threeDgraphics import cuboid
print("\nCuboid Area:", cuboid.area(4, 3, 2))
print("Cuboid Perimeter:", cuboid.perimeter(4, 3, 2))

from graphics.threeDgraphics.sphere import *
print("\nSphere Area:", area(5))
print("Sphere Perimeter (circumference):", perimeter(5))
