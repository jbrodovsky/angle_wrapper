import math

def to_pi(radians):
    return (radians + math.pi) % (2 * math.pi) - math.pi

def to_2pi(radians):
    return radians % (2 * math.pi)

def to_180(degrees):
    return (degrees + 180) % 360 - 180

def to_360(degrees):
    return degrees % 360
