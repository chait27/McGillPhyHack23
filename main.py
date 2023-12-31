from basicstuff import *
from montecarlo import *
from plotting import *
import numpy as np


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
    plot_spinsXYProjectionColor_inprogress(lattice)




def example_MC():
    basisvecs = (np.array([1, 0]), np.array([0, 1]))
    sites = (np.array([0, 0]),)

    uc = UnitCell(basisvecs, sites)
    size = (4, 4)

    uc.addInteraction(0, 0, -1*np.identity(3), (0, 1))
    # intmat1 = np.array([])
    uc.addInteraction(0, 0, -1*np.identity(3), (1, 0))
    uc.defineMagneticField(np.array([[1, 0,  0], ]))

    L = Lattice(unitcell=uc, size=size, spin_matrix=None)
    MC = MonteCarlo(L, thermalization_iter=0, measurement_iter=2000, T=0.1)
    H0 = L.Hamiltonian()

    MC.simulate()
    print(f'\nEnergies: {H0} -> {MC.get_latest_H()}')
    print(MC.get_parameters(), np.linalg.norm(MC.get_parameters()))


def exmaple_2():
    uc = UnitCell((np.array([0, 1]), np.array([1, 0])), (np.array([0, 0]),))
    x1 = np.array([[-1, 0, 0],[0, -1, 0], [0, 0, -1]])
    # x2 = np.array([[0, 0, 0.4],[0, 0, 0], [0, 0, -1]])
    uc.addInteraction(0, 0, x1, (0, 1))
    uc.addInteraction(0, 0, x1, (1, 0))

    lattice = Lattice(unitcell=uc, size=(6, 6), spin_matrix=None)

    MC = MonteCarlo(lattice, thermalization_iter=3000, measurement_iter=0, T=0.5)

    MC.simulate()




def temperature_example(min_temp, max_temp, resolution): 
    temp_range = np.geomspace(min_temp, max_temp, resolution)
    temp_magnetization = []
    
    for temp in temp_range:
        magnetizations =  []
        basisvecs = (np.array([1, 0]), np.array([0, 1]))
        sites = (np.array([0, 0]),)
        uc = UnitCell(basisvecs, sites)
        size = (6, 6)

        uc.addInteraction(0, 0, -1*np.identity(3), (0, 1))
        # intmat1 = np.array([])
        uc.addInteraction(0, 0, -1*np.identity(3), (1, 0))
        # uc.defineMagneticField(np.array([[0, 0,  0], ]))

        L = Lattice(unitcell=uc, size=size, spin_matrix=None)

        #for j in range(1):
        MC = MonteCarlo(L, thermalization_iter=3000, measurement_iter=1000, T=temp)
        H0 = L.Hamiltonian()
        MC.simulate()
        temp_magnetization.append(MC.get_parameters())
            #magnetizations.append(MC.get_parameters())
        #temp_magnetization.append(np.mean(magnetizations))
        
    return temp_magnetization

if __name__ == "__main__":
    temp_magnetization = temperature_example(0.1, 10, 40)
    np.save('temp_magnetization.npy', temp_magnetization)