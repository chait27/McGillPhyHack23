import numpy as np
from typing import Tuple


def randomSpin():
    theta, phi = np.random.uniform(0, np.pi), np.random.uniform(0, 2 * np.pi)
    return np.array([np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)])


def exchangeEnergy(s1, s2, intMatrix):
    return np.matmul(s1.T, np.matmul(intMatrix, s2))


class UnitCell:
    basisvec: tuple
    sites: tuple
    interactions: np.ndarray
    B: np.ndarray       # s x 3 matrix

    def __init__(self, basisvec: Tuple[np.ndarray], sites: Tuple[np.ndarray]):
        self.basisvec = basisvec
        self.sites = sites
        self.interactions = []
        self.B = np.zeros((len(sites), 3))

    def addInteraction(self, b1, b2, intMatrix, offset):
        self.interactions.append((b1, b2, intMatrix, offset))

    def defineMagneticField(self, B: np.ndarray):
        self.B = B


class Lattice:
    unitcell: UnitCell
    size: tuple
    lattice_vec: np.ndarray  # Nx2 matrix
    n_cells: int
    spin_matrix: np.ndarray  # Nx3 matrix

    def __init__(self, unitcell: UnitCell, size: tuple, spin_matrix: np.ndarray = None):
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
                         for _ in range(len(self.unitcell.sites))], dtype='float').T
                for _ in range(self.n_cells)], dtype='float'
            )

        else:
            self.spin_matrix = spin_matrix

    def Hamiltonian(self) -> float:
        H = 0
        for k2 in range(self.size[1]):
            for k1 in range(self.size[0]):
                pos1 = k1 + k2 * self.size[0]
                for i in range(len(self.unitcell.interactions)):
                    b1, b2, M, off = self.unitcell.interactions[i]
                    s1 = self.spin_matrix[pos1, :, b1]
                    s2 = self.spin_matrix[(
                        k1 + off[0]) % self.size[0] + (k2 * self.size[0] + off[1]) % self.size[1], :, b2]
                    H += exchangeEnergy(s1, s2, M)

                for i in range(len(self.unitcell.sites)):
                    H -= np.dot(self.spin_matrix[pos1,
                                :, i], self.unitcell.B[i, :])

        return H
