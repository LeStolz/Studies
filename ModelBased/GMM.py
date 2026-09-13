import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class Standardizer:
def __init__(self):
self.mean = 0
self.std = 0


def fit(self, X):
self.mean = np.mean(X, axis=0)
self.std = np.std(X, axis=0)


def transform(self, X):
return (X - self.mean) / self.std


class MixtureModel:
def __init__(self):
self.X = np.array([])
self.n = 0
self.m = 0
self.z = np.array([])
self.p = np.array([])
self.K = 0
self.cov = np.array([])
self.mean = np.array([])


def fit(self, X, z):
self.X = np.asarray(X)
self.n = self.X.shape[0]
self.m = self.X.shape[1] if self.X.ndim > 1 else 1
self.z = np.asarray(z)

self.K = len(np.unique(self.z))
self.p = np.array([np.mean(self.z == k) for k in range(self.K)])
self.cov = np.array([np.cov(self.X[self.z == k], rowvar=False) for k in range(self.K)])
self.mean = np.array([np.mean(self.X[self.z == k], axis=0) for k in range(self.K)])


def dist(self, k, x):
return 1 / ((2 * np.pi) ** (self.m/2) * np.linalg.det(self.cov[k]) ** (1/2)) * np.exp(-1/2 * (x - self.mean[k]).T @ np.linalg.inv(self.cov[k]) @ (x - self.mean[k]))


def t(self, k, x):
t = np.sum([self.p[l] * self.dist(l, x) for l in range(self.K)])
return self.p[k] * self.dist(k, x) / t


def predict(self, x):
return np.argmax([self.t(k, x) for k in range(self.K)])


X, z = make_blobs(
n_samples=500,
centers=3,
n_features=2,
cluster_std=[0.5, 2.0, 4.0],
random_state=42
)

s = Standardizer()
s.fit(X)
X = s.transform(X)


X_train, X_test, z_train, z_test = train_test_split(X)


mm = MixtureModel()
mm.fit(X, z)


for k in range(mm.K):
Xk = X[z == k]

plt.scatter(Xk[:, 0], Xk[:, 1], alpha=0.3)

plt.errorbar(
mm.mean[k, 0],
mm.mean[k, 1],
xerr=np.sqrt(mm.cov[k, 0, 0]),
yerr=np.sqrt(mm.cov[k, 1, 1]),
fmt='o',
color='black',
capsize=5
)

plt.show()