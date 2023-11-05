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

    def __init__(self, l: Lattice, thermalization_iter: int, measurement_iter: int, T: float):
        self.lattice = l
        self.thermalization_iter = thermalization_iter
        self.measurement_iter = measurement_iter
        self.T = T

    def simulate(self):
        new_lattice = lattice_copy(self.lattice)
        self.lattice = new_lattice
        k_B = 1

        for i in range(self.thermalization_iter + self.measurement_iter):
            for n in range(self.lattice.n_cells):
                for s in range(len(self.lattice.unitcell.sites)):
                    newest_lattice = lattice_copy(self.lattice)
                    H0 = self.lattice.Hamiltonian()

                    initial_spin = self.lattice.spin_matrix[n,
                                                            :, s]
                    # changing a spin randomly
                    temp = randomSpin()
                    newest_lattice.spin_matrix[n, :, s] = temp

                    dH = newest_lattice.Hamiltonian() - H0
                    k = np.random.random()

                    # if k > np.exp(-dH/(k_B*self.T)):
                    if k > np.exp(dH/(k_B*self.T)):
                        print(k)
                        self.lattice.spin_matrix[n,
                                                 :, s] = temp

                    if i < self.thermalization_iter:
                        pass

    def get_latest_H(self):
        return self.lattice.Hamiltonian()


def plot_spins(spins: np.ndarray):
    pass
