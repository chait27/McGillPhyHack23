import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize 
plt.rcParams['figure.figsize'] = (4,4)

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


def plot_spinsXYProjectionColor_inprogress(lattice: Lattice):
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

    massiveX, massiveY, massiveZ = [], [], []
    massiveXSpin, massiveYSpin, massiveZSpin = [], [], []

    for site in range(numSites):
        Xloc = np.array([lattice_vec[i][0][site] for i in range(numCell)])
        Yloc = np.array([lattice_vec[i][1][site] for i in range(numCell)])
        Zloc = np.array([0 for _ in range(numCell)])

        XSpin = np.array([spin_matrix[i][0][site] for i in range(numCell)])
        YSpin = np.array([spin_matrix[i][1][site] for i in range(numCell)])
        ZSpin = np.array([spin_matrix[i][2][site] for i in range(numCell)])

        massiveX, massiveY, massiveZ = np.concatenate((massiveX, Xloc)), np.concatenate((massiveY, Yloc)), np.concatenate((massiveZ, Zloc))
        massiveXSpin, massiveYSpin, massiveZSpin = np.concatenate((massiveXSpin, XSpin)), np.concatenate((massiveYSpin, YSpin)), np.concatenate((massiveZSpin, ZSpin))

        c = next(color)
        norm = np.sqrt(XSpin**2 + YSpin**2)
        #plt.quiver(Xloc, Yloc, XSpin, YSpin, color = 'black', label='Site ' + str(s) + " Spin")
        s += 1
    
    get_background(massiveX, massiveY, massiveZSpin, numSites*k1, k2, numSites)
    plt.quiver(massiveX, massiveY, massiveXSpin, massiveYSpin, color = 'black', label='Site ' + str(s) + " Spin")
    plt.show()

def get_background(X, Y, SpinZ, k1, k2, n):
   

    print(SpinZ.shape)
    Znew = np.zeros((k1, k2))
    for n in range(SpinZ.size-1):
        print((n)%k1, (n)//k1)
        Znew[(n)%k1, (n)//k1] = SpinZ[n]
    plt.pcolormesh(X.reshape([k1,k2]), Y.reshape([k1, k2]), Znew, alpha= 0.8, shading='gouraud', cmap='coolwarm', edgecolors='none')
    #plt.colorbar("ZSpin")
    #plt.pcolor(X.reshape([-1, X.size]),Y.reshape([Y.size, -1]), Znew)


"""plt.contourf(X,Y,Z=massiveZSpin, extent=(xgrid.min(), xgrid.max(), ygrid.min(), ygrid.max()))
    #Spin = np.sqrt(massiveXSpin**2 + massiveYSpin**2 + massiveZSpin**2)
    #cmap = plt.get_cmap('viridis')
    #norm = Normalize(vmin = Spin.min(), vmax = Spin.max())

    #spinz_grid = np.interp(X, massiveX, Spin)
    #colors = cmap(massiveZSpin)

    #plt.imshow(colors, extent=(xgrid.min(), xgrid.max(), ygrid.min(), ygrid.max()), origin='lower', interpolation='bicubic', aspect='auto')
    #plt.colorbar(label='TODO')

    #plt.contourf(xgrid, ygrid, colors, levels=100, extend='both')
    #plt.scatter(massiveX, massiveY, c=massiveZSpin, cmap=cmap)"""