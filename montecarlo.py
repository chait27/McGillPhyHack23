import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from typing import Callable, Tuple, List
from basicstuff import *


def simulator(Lattice: object, n_iterations: int):
    spins = np.repeat(np.ones(3), Lattice.size)    # Lattice.size x 3 array

    for i in range(n_iterations):
        site = np.random.randint(Lattice.size)
        # Calculate Hamiltonian's value for the state and call it H0
        initial_spin = spins[site]
        spins[site] = random_spin()

        # Let dH = H(spins) - H0
        # if np.random.random() <= exp(-dH/(k_BT)): continue
        # else: spins[site] = initial_spin


def plot_spins(spins: np.ndarray):
    pass
