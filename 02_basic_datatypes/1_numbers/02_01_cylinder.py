'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math

# define cylinder dimensions
radius = 3.14
height = 5

# calculate area of cylinder end faces
end_area = math.pi*(radius**2)

# calculate area of cylinder side
side_area = 2*math.pi*radius*height

# calculate and print volume
vol = end_area*height
print("The volume is ", vol)

# calculate and print the surface area
sur_area = 2*end_area + side_area
print("The surface area is ", sur_area)
