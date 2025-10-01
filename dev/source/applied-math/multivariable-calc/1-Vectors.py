import sys
sys.path.append('../../')

import matplotlib.pyplot as plt
from tools.plot_line import plot_line_3D
from tools.AngleAnnotation import AngleAnnotation

# =========== SETUP ==============#
ax = plt.figure().add_subplot(projection='3d')
ax.view_init(elev=20, azim=-115, roll=0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Define points A and B (hypotenuse endpoints)
A = (1, 1, 1)
B = (3, 5, 4)

# Now we setup the other 2 points.
C = (B[0], B[1], A[2])
D = (C[0], A[1], A[2])

# Alignments
aa=('right', 'bottom')
ba=('left', 'bottom')
ca=('left', 'top')

plot_line_3D(A, B, ax, ("A", "B"))
plot_line_3D(A, D, ax, ("A", "D"), style = 'b--')
plot_line_3D(D, C, ax, ("D", "C"), style = 'b--')
plot_line_3D(C, A, ax, ("C", "A"), style = 'b--')
plot_line_3D(C, B, ax, ("C", "B"), style = "b--")

plt.show()