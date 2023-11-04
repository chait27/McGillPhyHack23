import numpy as np
from typing import Tuple


def randomSpin():
    theta, phi = np.random.uniform(0, np.pi), np.random.uniform(0, 2 * np.pi)
    return np.array([np.cos(theta) * np.cos(phi), np.cos(theta) * np.sin(phi), np.sin(theta)])


def exchangeEnergy(s1, s2, intMatrix):
    return np.matmul(s1.T, np.matmul(intMatrix, s2))


class UnitCell:
    basisvec: tuple
    sites: tuple
    interactions: np.ndarray

    def __init__(self, basisvec: Tuple[np.ndarray], sites: Tuple[np.ndarray]):
        self.basisvec = basisvec
        self.sites = sites
        self.interactions = []

    def addInteraction(self, b1, b2, intMatrix, offset):
        self.interactions.append((b1, b2, intMatrix, offset))


class Lattice:
    unitcell: UnitCell
    size: tuple
    lattice_vec: np.ndarray  # Nx2 matrix
    n_cells: int
    spin_matrix: np.ndarray  # Nx3 matrix

    def __init__(self, size: tuple, unitcell: UnitCell, spin_matrix: np.ndarray = None):
        self.unitcell = unitcell
        self.size = size

        self.n_cells = size[0]*size[1]

        self.lattice_vec = np.zeros(
            shape=(self.n_cells, 2, len(self.unitcell.sites)))

        for k2 in range(self.size[1]):
            for k1 in range(self.size[0]):
                for (k, site) in enumerate(self.unitcell.sites):
                    self.lattice_vec[k1+k2*size[0], :, k] = site + k1*self.unitcell.basisvec[0] + \
                        k2*self.unitcell.basisvec[1]

        if spin_matrix is None:
            self.spin_matrix = np.array([
                np.array([randomSpin()
                         for _ in range(len(self.unitcell.sites))]).T
                for _ in range(self.n_cells)]
            )

        else:
            self.spin_matrix = spin_matrix

    def Hamiltonian(self) -> float:
        H = 0
        for k2 in range(self.size[1]):
            for k1 in range(self.size[0]):
                pos1 = k1 + k2 * self.size[1]
                for i in range(len(self.unitcell.interactions)):
                    b1, b2, M, off = self.unitcell.interactions[i]
                    s1  = self.spin_matrix[pos1, :, b1]
                    s2  = self.spin_matrix[(k1 + off[0]) % self.size[0] + (k2 * self.size[1] + off[1]) % self.size[1],  :, b2]
                    H += exchangeEnergy(s1, s2, M)

                    return H 
