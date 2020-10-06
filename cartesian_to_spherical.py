import numpy as np

def convert_to_spherical(x,y,z):
    r = np.sqrt(np.square(x)+np.square(y)+np.square(z))
    theta = 1/np.cos(z/r)
    phi = 1/np.tan(y/x)

    return (r,phi,theta)


def reverse_2(r,phi,theta):
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)

    return (x,y,z)