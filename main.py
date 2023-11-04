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
    sites = (np.array([1, 1]))

    uc = UnitCell(basisvecs, sites)
    size = (1, 1)

    L = Lattice(size=size, unitcell=uc, spin_matrix=None)
    MC = MonteCarlo(L, thermalization_iter=5, measurement_iter=10, T=1)

    H0 = L.Hamiltonian()
    print(H0)
    print(MC.get_latest_H())


example_MC()
