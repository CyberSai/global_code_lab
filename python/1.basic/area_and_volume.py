import math

radius = int(raw_input("Please Enter Radius "))

surface_area = 4 * math.pi * radius ** 2

volume = 4 / 3.0 * math.pi * radius ** 3

print "The surface area of a sphere with " + str(radius) + " is " + str(surface_area)

print "The volume of a sphere with " + str(radius) + " is " + str(volume)

