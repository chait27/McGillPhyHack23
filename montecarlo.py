import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import copy

from typing import Callable, Tuple, List
from basicstuff import *


class MonteCarlo:
    l: Lattice
    thermalization_iter: int
    measurement_iter: int

    def __init__(self, l: Lattice, thermalization_iter: int, measurement_iter: int):
        self.lattice = l
        self.thermalization_iter = thermalization_iter
        self.measurement_iter = measurement_iter

    def simulator(self, n_iterations: int):
        new_lattice = lattice_copy(self.lattice)
        self.lattice = new_lattice

        for i in range(n_iterations):
            site = np.random.randint(new_lattice.n_cells)
            # Calculate Hamiltonian's value for the state and call it H0
            initial_spin = new_lattice.spin_matrix[site]
            new_lattice.spin_matrix[site] = randomSpin()

            # Let dH = H(spins) - H0
            # if np.random.random() <= exp(-dH/(k_BT)): continue
            # else: spins[site] = initial_spin


def lattice_copy(l: Lattice) -> Lattice:
    return Lattice(l.unitcell, l.size, l.spin_matrix)


def plot_spins(spins: np.ndarray):
    pass
