import numpy as np

def convert_to_cylindrical(x,y,z):
    p = np.sqrt(np.square(x)+np.square(y))
    phi = 1/np.tan(y/z)
    z = z
    return (p,phi,z)



def reverse_1(p,phi,zee):
    x = p*np.sin(phi)
    y = p*np.cos(phi)
    z = zee
    return (x,y,z)
