import numpy as np
from typing import Tuple


def randomSpin():
    theta, phi = np.random.uniform(0, np.pi), np.random.uniform(0, 2 * np.pi)
    return np.array([np.cos(theta) * np.cos(phi), np.cos(theta) * np.sin(phi), np.sin(theta)])


def exchangeEnergy(s1, s2, intMatrix):
    return np.dot(s1, np.dot(intMatrix, s2))


class UnitCell:
    basisvec: Tuple[np.ndarray]
    sites: Tuple[np.ndarray]
    interactions: list

    def __init__(self, basisvec: Tuple[np.ndarray], sites: Tuple[np.ndarray]):
        self.basisvec = basisvec
        self.sites = sites
        self.interactions = []

    def addInteraction(self, b1, b2, intMatrix, offset):
        self.interactions.append((b1, b2, intMatrix, offset))


class Lattice:
    unitcell: UnitCell
    size: Tuple[int]
    lattice_vec: np.ndarray  # n_sites x 2 x len(unitcell.sites) matrix
    n_cells: int
    spin_matrix: np.ndarray  # n_sites x 3 x len(unitcell.sites) matrix

    def __init__(self,  unitcell: UnitCell, size: tuple):
        self.unitcell = unitcell
        self.size = size
        self.n_cells = size[0]*size[1]
        self.lattice_vecs = np.zeros(
            shape=(self.n_cells, 2, len(self.unitcell.sites)))

        # Assumes we have one unique site
        for k1 in range(self.size[0]):
            for k2 in range(self.size[1]):
                for (k, site) in enumerate(self.unitcell.sites):
                    self.lattice_vecs[k1+k2*size[1], :, k] = site + k1 * \
                        self.unitcell.basisvec[0] + \
                        k2*self.unitcell.basisvec[1]

        self.spin_matrix = np.array(
            [[randomSpin() for _ in range(self.n_cells)] for _ in self.unitcell.sites])

    def Hamiltonian(self):
        pass


if __name__ == '__main__':
    # Example
    uc = UnitCell(basisvec=(np.array([1, 0]), np.array([0, 1])), sites=(
        np.array([1, 1]), np.array([1, 1.5])))
    L = Lattice(uc, size=(3, 3))

    print(L.spin_matrix)
