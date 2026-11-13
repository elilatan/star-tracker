import numpy as np
from catalog import load_catalog

#Goals:
#get x = cos(dec)cosa
#y = cos(dec)sina
#z = sin(dec)

#Parameters:
#Ra - Right ascension (treated as longitude)
#dec - declination (treated as latitude)
#
#This function takes degrees and returns unit vectors
def vector_conversion(ra, dec):

    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)

    #z
    z = np.sin(dec_rad)

    #x
    x = np.cos(dec_rad) * np.cos(ra_rad)

    #y 
    y = np.cos(dec_rad) * np.sin(ra_rad)


    #append everything together
    vector = np.column_stack((x, y, z))

    return vector

if __name__ == "__main__":

    test = vector_conversion(0, 0)
    test2 = vector_conversion(90, 0)
    test3 = vector_conversion(90, 90)
    print(f"Test 1: {test}, Test 2: {test2}, Test 3: {test3}")
    stars = load_catalog("data/asu.tsv")
    star_vectors = vector_conversion(stars[:, 0], stars[:, 1])
    star_norms = np.linalg.norm(star_vectors, axis=1)
    print(f"Maximum: {np.max(star_norms)}, Minimum: {np.min(star_norms)}")
    
