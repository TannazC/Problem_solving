import math

#area rectangle
def area_rectangle(length, width):
    area=length*width
    return area

#area circle
def area_circle(radius):
    area= (math.pi)*(radius**2)
    return area

#circumference circle
def circumference(radius):
    circum= 2*(math.pi)*radius
    return circum

#volume rec prism
def volume_rectangular_prism(length, width, height):
    volume= length*width*height
    return volume

#volume cylinder
def volume_cylinder(radius, height):
    circle=area_circle(radius)
    volume=circle*height
    return volume

def surface_area_rectangular_prism(length, width, height):
    faces1=length*width
    faces2=length*height
    faces3=width*height
    SA=faces1+faces2+faces3
    return SA

def surface_area_cylinder(radius, height):
    circleface= area_circle(radius)
    rectangleface=(circumference(radius))*height
    SA= circleface+rectangleface
    return SA