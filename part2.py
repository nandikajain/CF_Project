import numpy as np

R = np.array([
    [1, 2, -1, -1],
    [1, 2, -1, 1],
    [3, 4, 5, 3],
])

WALS = np.array([
    [1, 1, 0.56, 0.87],
    [1, 1, 0.34, 1],
    [1, 1, 1, 1],
])

ZERO_INJECTED = np.random.random(R.shape)

theta =  0.5

for i in range(len(R)):
    for j in range(len(R[i])):
        if WALS[i][j] != 1 and WALS[i][j] < theta:
            ZERO_INJECTED[i][j] = 0
        else:
            ZERO_INJECTED[i][j] = R[i][j]

print(ZERO_INJECTED)