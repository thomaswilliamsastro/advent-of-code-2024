import numpy as np
import time

# Load in the lists
l1, l2 = np.loadtxt(
    "input.txt",
    unpack=True,
)

start = time.time()

# Part 1: distances
l1_sort = np.sort(l1)
l2_sort = np.sort(l2)

diff = l2_sort - l1_sort
total_dist = np.sum(np.abs(diff))
total_dist = int(total_dist)
print(f"Total distance: {total_dist}. Took {time.time() - start:.2e} s")

# Part 2: similarities

start = time.time()

n1, count1 = np.unique(l1, return_counts=True)
n2, count2 = np.unique(l2, return_counts=True)

total_count = [
    count * n * count2[np.where(n2 == n)][0]
    for (n, count) in zip(n1, count1)
    if n in n2
]

total_count = int(np.sum(total_count))

print(f"Total count: {total_count}. Took {time.time() - start:.2e} s")

print("Complete!")
