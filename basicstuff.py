import numpy as np


def randomSpin():
    theta, phi = np.random.uniform(0, np.pi), np.random.uniform(0, 2 * np.pi)
    return (np.cos(theta) * np.cos(phi), np.cos(theta) * np.sin(phi), np.sin(theta))


def exchangeEnergy(s1, s2, intMatrix):
    return np.dot(s1, np.dot(intMatrix, s2))


class UnitCell:
    basisvec: tuple
    sites: tuple
    interactions: np.ndarray

    def init(self, basisvec, sites):
        self.basisvec = basisvec
        self.sites = sites
        self.interactions = []

    def addInteraction(self, b1, b2, intMatrix, offset):
        self.interactions.append((b1, b2, intMatrix, offset))


class Lattice:
    unitcell: UnitCell
    size: tuple
    latticevec: np.ndarray

    def __init__(self):
        pass

    def Hamiltonian(self):
        pass
