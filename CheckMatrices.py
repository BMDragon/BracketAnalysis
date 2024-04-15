import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

matName = 'ALvsAL'
matrix = np.load(matName + 'matrix.npy')

seeding = np.arange(1, 17, 1)

fig1, ax1 = plt.subplots()
im1 = ax1.imshow(np.divide(matrix[:,:,0], matrix[:,:,1]))

print(matrix[0,0,1])

ax1.set_title("At Large teams vs At Large teams: higher seed success rate")
ax1.set_xlabel("Lower seed")
ax1.set_ylabel("Higher seed")
cbar = ax1.figure.colorbar(im1, ax=ax1)
fig1.tight_layout()
plt.show()