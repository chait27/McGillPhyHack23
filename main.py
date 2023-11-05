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
    sites = (np.array([0, 0]),)

    uc = UnitCell(basisvecs, sites)
    size = (1, 3)

    uc.addInteraction(0, 0, -1*np.identity(3), (0, 1))

    L = Lattice(unitcell=uc, size=size, spin_matrix=None)
    MC = MonteCarlo(L, thermalization_iter=20, measurement_iter=0, T=0.1)
    H0 = L.Hamiltonian()

    print(L.spin_matrix)
    MC.simulate()
    print(f'\nEnergies: {H0} -> {MC.get_latest_H()}')
    print(MC.lattice.spin_matrix)


example_MC()
