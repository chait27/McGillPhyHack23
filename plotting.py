import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize 
plt.rcParams['figure.figsize'] = (5,5)

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
    (k1, k2) = lattice.size
    lattice_vec = lattice.lattice_vec  # n_cells x 2 x len(unitcell.sites) matrix
    numCell = lattice.n_cells
    spin_matrix = lattice.spin_matrix  # n_cells x 3 x len(unitcell.sites) matrix

    numCell, _, numSites = spin_matrix.shape
    color, s = iter(plt.cm.rainbow(np.linspace(0, 1, numSites))), 0
    for site in range(numSites):
        Xloc = [lattice_vec[i][0][site] for i in range(numCell)]
        Yloc = [lattice_vec[i][1][site] for i in range(numCell)]
        Zloc = [0 for i in range(numCell)]
        c = next(color)
        plt.scatter(Xloc, Yloc, color = c, label = 'Site ' + str(s) + " Spin")
        s += 1
    plt.legend()
    plt.show()

        
def plot_spins3D(lattice: Lattice):
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

        XSpin = [spin_matrix[i][0][site] for i in range(numCell)]
        YSpin = [spin_matrix[i][1][site] for i in range(numCell)]
        ZSpin = [spin_matrix[i][2][site] for i in range(numCell)]
        
        c = next(color)
        ax.quiver(Xloc, Yloc, Zloc, XSpin, YSpin, ZSpin, length=0.5, normalize=True, color = 'black', label='Site ' + str(s) + " Spin")
        #ax.scatter(Xloc, Yloc, Zloc, color = c)
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


def plot_spinsXYProjection(lattice: Lattice):
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

    for site in range(numSites):
        Xloc = [lattice_vec[i][0][site] for i in range(numCell)]
        Yloc = [lattice_vec[i][1][site] for i in range(numCell)]
        Zloc = [0 for i in range(numCell)]

        XSpin = np.array([spin_matrix[i][0][site] for i in range(numCell)])
        YSpin = np.array([spin_matrix[i][1][site] for i in range(numCell)])
        ZSpin = np.array([spin_matrix[i][2][site] for i in range(numCell)])

        
        c = next(color)
        norm = np.sqrt(XSpin**2 + YSpin**2)
        plt.quiver(Xloc, Yloc, XSpin/norm, YSpin/norm, color = 'black', label='Site ' + str(s) + " Spin")
        #plt.scatter(Xloc, Yloc, color = c)
        s += 1

    plt.xlabel('X')
    plt.xlim(0, k1)
    plt.ylabel('Y')
    plt.ylim(0, k2)
    plt.title("Spin Structure")
    plt.show()


def plot_spinsXYProjectionColor_inprogress(lattice: Lattice, i: int, temp: float):
    fig, ax = plt.subplots(1, 1)

    (k1, k2) = lattice.size
    # n_cells x 2 x len(unitcell.sites) matrix
    lattice_vec = lattice.lattice_vec
    numCell = lattice.n_cells
    # n_cells x 3 x len(unitcell.sites) matrix
    spin_matrix = lattice.spin_matrix

    numCell, _, numSites = spin_matrix.shape

    if (k1 != numCell // k2):
        print("Size Error")
        print(k1, k2, numCell)
        return None

    color, s = iter(plt.cm.rainbow(np.linspace(0, 1, numSites))), 0

    # massiveX, massiveY, massiveZ = [], [], []
    # massiveXSpin, massiveYSpin, massiveZSpin = [], [], []

    massiveX = np.array(lattice_vec[:, 0, :]).flatten(order='F')
    massiveY = np.array(lattice_vec[:, 1, :]).flatten(order='F')
    massiveZSpin = np.array(spin_matrix[:, 2, :]).flatten(order='F')

    get_background(massiveX, massiveY, massiveZSpin,
                   numSites*k1, k2, numSites, fig, ax)

    for site in range(numSites):
        Xloc = lattice_vec[:, 0, site]
        Yloc = lattice_vec[:, 1, site]
        Zloc = np.array([0 for _ in range(numCell)])

        XSpin = spin_matrix[:, 0, site]
        YSpin = spin_matrix[:, 1, site]

        c = next(color)
        norm = np.sqrt(XSpin**2 + YSpin**2)
        ax.quiver(Xloc, Yloc, XSpin, YSpin, color='black',
                  label='Site ' + str(s) + " Spin")
        s += 1
    s = str(round(temp, 2))
    s = s.replace('.', 'p')
    label = "Iteration " + str(i)+ "-Temp " +s+".jpeg"
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Position (y)')
    ax.set_title('Position Space Spin Configuration' + "-Temp " + str(round(temp, 2)))
    fig.tight_layout()
    plt.savefig(label, dpi=600, bbox_inches='tight')
    # plt.show()

def get_background(X, Y, SpinZ, k1, k2, n, fig, ax):

    Znew = np.zeros((k1, k2))
    for n in range(SpinZ.size-1):
        #print((n) % k1, (n)//k1)
        Znew[(n) % k1, (n)//k1] = SpinZ[n]

    c = ax.pcolormesh(X.reshape([k1, k2]), Y.reshape(
        [k1, k2]), Znew.T, alpha=1, shading='gouraud', cmap='coolwarm', edgecolors='none', vmin=-1, vmax=1)

    cbar = fig.colorbar(c, ax=ax)
    cbar.set_label('Spin in Z-direction', rotation=270)