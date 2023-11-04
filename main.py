from basicstuff import *
from montecarlo import *
from plotting import *


def example_1():
    basisvecs = (np.array([1, 0]), np.array([0, 1]))
    # sites = (np.array([1, 1]), np.array([1, 2]))
    sites = (np.array([0, 0]), np.array([0, 0.5]))

    uc = UnitCell(basisvecs, sites)
    size = (4, 4)
    uc.addInteraction(0, 0, np.identity(4), (0, 1))

    lattice = Lattice(size=size, unitcell=uc, spin_matrix=None)

    print(lattice.spin_matrix.shape)
    plot_basic_unitcell(lattice)
    plot_spins(lattice)


def example_MC():
    basisvecs = (np.array([1, 0]), np.array([0, 1]))
    sites = (np.array([1, 1]), np.array([1, 2]))

    uc = UnitCell(basisvecs, sites)
    size = (1, 1)
    uc.addInteraction(b1=0, b2=1, intMatrix=np.identity(3), offset=(0, 0))
    uc.addInteraction(b1=2, b2=0, intMatrix=np.identity(3), offset=(0, 0))
    uc.addInteraction(b1=1, b2=2, intMatrix=np.identity(3), offset=(0, 0))

    L = Lattice(size=size, unitcell=uc, spin_matrix=None)
    MC = MonteCarlo(L, thermalization_iter=5, measurement_iter=10)
    print(MC.get_latest_H())
