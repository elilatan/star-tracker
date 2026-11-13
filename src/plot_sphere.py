#plot_sphere
import numpy as np
import matplotlib.pyplot as plt
from catalog import load_catalog
from coords import vector_conversion

if __name__ == "__main__":
    stars = load_catalog("data/asu.tsv")
    star_vectors = vector_conversion(stars[:, 0], stars[:, 1])


    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(star_vectors[:, 0], star_vectors[:, 1], star_vectors[:, 2], s=0.01, c='red', marker='o', depthshade=True)
    ax.set_box_aspect((1,1,1))
    

    ax.set_xlabel('X (toward RA 0)')
    ax.set_ylabel('Y (toward RA = 90, dec = 0)')
    ax.set_zlabel('Z (north celestial pole)')

    plt.savefig("plots/star_sphere.png", dpi=150)
    plt.show()