import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import copy

from typing import Callable, Tuple, List
from basicstuff import *


def lattice_copy(l: Lattice) -> Lattice:
    return Lattice(l.unitcell, l.size, copy.deepcopy(l.spin_matrix))


class MonteCarlo:
    l: Lattice
    thermalization_iter: int
    measurement_iter: int

    def __init__(self, l: Lattice, thermalization_iter: int, measurement_iter: int, T: float = 1):
        self.lattice = l
        self.thermalization_iter = thermalization_iter
        self.measurement_iter = measurement_iter
        self.T = T

    def simulator(self, n_iterations: int):
        new_lattice = lattice_copy(self.lattice)
        self.lattice = new_lattice
        k_B = 1

        for i in range(n_iterations):
            site = np.random.randint(new_lattice.n_cells)
            H0 = self.lattice.Hamiltonian()

            initial_spin = self.lattice.spin_matrix[site]
            # changing a spin randomly
            self.lattice.spin_matrix[site] = randomSpin()

            dH = self.lattice.Hamiltonian() - H0

            if np.random.random() <= np.exp(-dH/(k_B*self.T)):
                continue
            else:
                self.lattice.spin_matrix[site] = initial_spin

    def get_latest_H(self):
        return self.lattice.Hamiltonian()


def plot_spins(spins: np.ndarray):
    pass
