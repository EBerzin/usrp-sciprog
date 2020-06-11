import numpy as np
import matplotlib.pyplot as plt
import time
import sys


def darts(N):
    x = np.random.rand(N)
    y = np.random.rand(N)
    return x,y


def estimate_pi(N):
    x,y = darts(N)
    r = np.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    r_bool = (r <= 0.5)
    pi_estimate = (np.sum(r_bool) / N) * 4
    return pi_estimate


def plot_circle(xcenter,ycenter,radius):
    theta = np.linspace(0, 2 * np.pi, 1000)
    xpoints = radius* np.cos(theta) + xcenter
    ypoints = radius * np.sin(theta) + ycenter
    plt.plot(xpoints,ypoints, 'k')


def timer(function, argument):
    start_time = time.time()
    function(argument)
    end_time = time.time()
    return end_time - start_time


def plot_darts(N):
    x,y = darts(N)
    plt.figure()
    r = np.sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)
    plt.scatter(x[r < 0.5], y[r < 0.5], s=5, c='r')
    plt.scatter(x[r > 0.5], y[r > 0.5], s=5, c='b')
    plot_circle(0.5, 0.5, 0.5)
    plt.show()


# Plots darts for N = 1000
plot_darts(10000)

# Times and calculates values of pi for several values of N.
N = 100000 * np.arange(1,11)
times = []
estimate_precision = []

for n in N:
    times.append(timer(estimate_pi, n))
    estimate_precision.append((abs(np.pi - estimate_pi(n)) / np.pi) *100)


# Plot of Execution Time
plt.figure()
plt.scatter(N,times)
plt.xlabel("Number of Darts")
plt.ylabel("Execution Time(s)")
plt.show()


# Plot of Percent Error
plt.figure()
plt.scatter(N,estimate_precision)
plt.xlabel("Number of Darts")
plt.ylabel("Percent Error")
plt.show()

# Histogram of estimates and some statistics
N = 1000

estimates = []
repeats = 100

for i in range(100):
    estimates.append(estimate_pi(N))

plt.figure()
plt.hist(estimates)
print("Mean: " + str(np.mean(estimates)))
print("Standard Deviation: " + str(np.std(estimates)))
plt.show()

