import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from basicstuff import *

def plot_basic_unitcell(lattice: Lattice):
    uc = lattice.unitcell
    sites = uc.sites

    color = iter(plt.cm.rainbow(np.linspace(0, 1, len(sites))))
    for site in sites:
        c = next(color)
        plt.scatter(site[0], site[1], color = c)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.title("Unit Cell")
    plt.show()

def plot_lattice(lattice: Lattice):
    pass
        

def plot_spins(lattice: Lattice):
    uc = lattice.unitcell
    (k1, k2) = lattice.size
    lattice_vec = lattice.lattice_vec  # n_cells x 2 x len(unitcell.sites) matrix
    numCell = lattice.n_cells
    spin_matrix = lattice.spin_matrix  # n_cells x 3 x len(unitcell.sites) matrix

    numCell, _, numSites = spin_matrix.shape
    
    if (k1 != numCell // k2):
        print("Size Error")
        print(k1, k2, numCell)
        return None
    
    color, s = iter(plt.cm.rainbow(np.linspace(0, 1, numSites))), 0

    ax = plt.figure().add_subplot(projection='3d')
    for site in range(numSites):
        Xloc = [lattice_vec[i][0][site] for i in range(numCell)]
        Yloc = [lattice_vec[i][1][site] for i in range(numCell)]
        Zloc = [0 for i in range(numCell)]
        #print(Xloc,Yloc,Zloc)
        #X, Y, Z = np.meshgrid(Xloc, Yloc, Zloc)

        XSpin = [spin_matrix[i][0][site] for i in range(numCell)]
        YSpin = [spin_matrix[i][1][site] for i in range(numCell)]
        ZSpin = [spin_matrix[i][2][site] for i in range(numCell)]
        
        c = next(color)
        ax.quiver(Xloc, Yloc, Zloc, XSpin, YSpin, ZSpin, length=0.5, normalize=True, color = c, label='Site ' + str(s) + " Spin")
        s += 1
    
    ax.set_xlabel('X')
    ax.set_xlim(-1, k1)
    ax.set_ylabel('Y')
    ax.set_ylim(-1, k2)
    ax.set_zlabel('Z')
    ax.set_zlim(-1, 1)

    # Show the 3D plot
    plt.legend()
    plt.title("Spin Structure")
    plt.show()