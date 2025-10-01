import matplotlib.pyplot as plt
from tools.plot_line import plot_line 
from tools.AngleAnnotation import AngleAnnotation

# Define points A and B (hypotenuse endpoints)
A = (1, 1)
B = (6, 4)

# Calculate the third point C to form a right triangle
# We'll make C share x with A and y with B (right angle at C)
C = (B[0], A[1])

# Alignments
aa=('right', 'bottom')
ba=('left', 'bottom')
ca=('left', 'top')

def plot_init_line():
    plot_line(A, B, ("A","B"), a_alignment=aa, b_alignment=ba)

def plot_right_triangle():
    plot_line(A, C, line_label=r"$x$", a_alignment=aa, b_alignment=ca, l_alignment=('center','top'))
    plot_line(B, C, line_label=r"$y$", a_alignment=ba, b_alignment=ca, l_alignment=('left','center'))
    plot_line(A, B, line_label=r"$z$", a_alignment=aa, b_alignment=ba, l_alignment=('center','bottom'))

def plot_all_triangles():
    plot_right_triangle()
    x_extended = (B[1] - A[1])**2 / (B[0] - A[0])
    x_ext_point = (B[0] + x_extended, A[1])
    plot_line(C, x_ext_point, line_label=r"$x_e$", l_alignment=('left','top'), style='k--')
    plot_line(B, x_ext_point, style='k--')
    
    ax = plt.gca()
    AngleAnnotation(A, C, B, size=100, ax=ax, text=r"$\alpha$", textposition="inside")
    AngleAnnotation(B, C, x_ext_point, size=100,ax=ax, text=r"$\alpha$", textposition="inside")
    AngleAnnotation(B, A, C, size=100, ax=ax, text=r"$\beta$", textposition="inside")
    AngleAnnotation(x_ext_point, B, C, size=100, ax=ax, text=r"$\beta$", textposition="inside")
    AngleAnnotation(C, B, A, size=200, ax=ax, color="red")
    AngleAnnotation(B, A, x_ext_point, size=200, ax=ax, color="red")

# ========== UTILITY ============= #
def plot_setup():
    plt.figure(figsize=(4, 4))
    plt.axis('off')

def plot_setup_all():
    fig, ax = plt.subplots(figsize=(6.6, 4))
    fig.canvas.draw()  # Need to draw the figure to define renderer
    plt.axis('off')

def plot(setup, plot_func):
    setup()
    plot_func()
    plt.show()
# ================================ #
plot(plot_setup, plot_init_line)
plot(plot_setup, plot_right_triangle)
plot(plot_setup_all, plot_all_triangles)
# ================================ #

