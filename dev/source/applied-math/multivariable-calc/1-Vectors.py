import sys
sys.path.append('../../')

import matplotlib.pyplot as plt
import numpy as np
import math
from tools.plot_line import plot_line_2D, plot_line_3D
from tools.AngleAnnotation import AngleAnnotation

def setup():
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    return ax

def figure_1():
    ax = setup()
    ax.view_init(elev=20, azim=-115, roll=0)

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

def figure_2_main():
    ax = plt.figure().add_subplot()
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    x0 = (1, 1)
    vec_a = (2, 6)
    vec_b = (7, 3)
    p1 = (x0[0]+vec_a[0], x0[1]+vec_a[1])
    p2 = (x0[0]+vec_b[0], x0[1]+vec_b[1])

    ax.quiver(x0[0], x0[1], vec_a[0], vec_a[1], angles='xy', scale_units='xy', scale=1)
    ax.text(vec_a[0] - 0.1, vec_a[1]-0.3, r'$\vec a$', fontsize=15)
     
    ax.quiver(x0[0], x0[1], vec_b[0], vec_b[1], angles='xy', scale_units='xy', scale=1)
    ax.text(vec_b[0] - 0.1, vec_b[1]-0.3, r'$\vec b$', fontsize=15)
    
    vec_diff = (vec_a[0] - vec_b[0], vec_a[1]-vec_b[1])
    ax.quiver(p2[0], p2[1], vec_diff[0], vec_diff[1], angles='xy', scale_units='xy', scale=1)
    ax.text(p2[0] - 2, p2[1] + 2, r'$\vec b - \vec a = \vec c$', fontsize=15)

    AngleAnnotation(x0, p2, p1, ax=ax, size=200, text=r"$\theta$")
    return x0, vec_a, vec_b, p1, p2

def figure_2():
    figure_2_main()
    plt.axis('off')
    plt.show()

def figure_3():
    x0, vec_a, vec_b, p1, p2 = figure_2_main()
    vec_ax = vec_a[0] - x0[0]
    vec_ay = vec_a[1] - x0[1]
    vec_bx = vec_b[0] - x0[0]
    vec_by = vec_b[1] - x0[1]
    a_dot_b = vec_ax * vec_bx + vec_ay * vec_by
    a_length = math.sqrt(vec_ax**2 + vec_ay**2)
    b_length = math.sqrt(vec_bx**2 + vec_by**2)
    a_proj_length = a_dot_b / b_length
    b_unit = (vec_b[0]/b_length, vec_b[1]/b_length)
    a_proj = (b_unit[0]*a_proj_length, b_unit[1]*a_proj_length)
    p3 = (x0[0]+a_proj[0], x0[1]+a_proj[1])
    
    plot_line_2D(p1, p3, style='b--')
    plot_line_2D(x0, p3, style='b-', line_label=r"$a\cos \theta = \vec a_{proj}$", l_alignment=('left', 'top'))
    plt.axis('off')
    plt.show()

def figure_4():
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([0, 7])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.view_init(elev=20, azim=-115, roll=20)

    # plane
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    xx, yy = np.meshgrid(x, y)
    z = 0.2* xx + 0.2* yy + 4

    p0  = (0, 0 , 4)
    p1 = (3, -3, 4)
    p2 = (1, 1, 4.4)

    vec_p0p1 = np.array(p1) - np.array(p0)
    vec_p0p2 = np.array(p2) - np.array(p0)

    ax.plot_surface(xx, yy, z, alpha = 0.25)
    ax.scatter(xs=[p0[0],p1[0], p2[0]], ys = [p0[1], p1[1], p2[1]], zs = [p0[2], p1[2], p2[2]], s = 20, color = 'black')
    
    ax.quiver(0,0,0, p0[0],p0[1],p0[2], color='black', arrow_length_ratio=0.2)
    ax.text(0,0, p0[2]/2, r'$\vec r_0$', fontsize=15)

    ax.quiver(p0[0], p0[1], p0[2], vec_p0p1[0], vec_p0p1[1], vec_p0p1[2], color='black', arrow_length_ratio=0.2)
    ax.text(p1[0], p1[1], p1[2], r'P1', fontsize=15)

    ax.quiver(p0[0], p0[1], p0[2], vec_p0p2[0], vec_p0p2[1], vec_p0p2[2], color='black', arrow_length_ratio=0.2)
    ax.text(p2[0], p2[1], p2[2], r'P2', fontsize=15)

    ax.quiver(p0[0], p0[1], p0[2], -0.2, -0.2, 1, length=2, color='black', arrow_length_ratio=0.2)
    ax.text(p0[0]-1, p0[1]+0.5, p0[2]+1, r'$\hat n$', fontsize=15)

    plt.axis('off')
    plt.show()

def figure_5():
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([0, 7])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.view_init(elev=20, azim=-115, roll=20)

    # plane
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    xx, yy = np.meshgrid(x, y)
    z = 0.2* xx + 0.2* yy + 4

    p0  = (0, 0 , 4)
    p1 = (3, -3, 4)
    p2 = (1, 1, 4.4)

    vec_p0p1 = np.array(p1) - np.array(p0)
    vec_p0p2 = np.array(p2) - np.array(p0)

    ax.plot_surface(xx, yy, z, alpha = 0.25)
    ax.scatter(xs=[p0[0],p1[0], p2[0]], ys = [p0[1], p1[1], p2[1]], zs = [p0[2], p1[2], p2[2]], s = 20, color = 'black')
    
    ax.quiver(0,0,0, p0[0],p0[1],p0[2], color='black', arrow_length_ratio=0.2)
    ax.text(0,0, p0[2]/2, r'$\vec r_0$', fontsize=15)

    ax.quiver(p0[0], p0[1], p0[2], vec_p0p1[0], vec_p0p1[1], vec_p0p1[2], color='black', arrow_length_ratio=0.2)
    ax.text(p1[0], p1[1], p1[2], r'P1', fontsize=15)

    ax.quiver(p0[0], p0[1], p0[2], vec_p0p2[0], vec_p0p2[1], vec_p0p2[2], color='black', arrow_length_ratio=0.2)
    ax.text(p2[0], p2[1], p2[2], r'P2', fontsize=15)

    ax.quiver(p0[0], p0[1], p0[2], -0.2, -0.2, 1, length=2, color='black', arrow_length_ratio=0.2)
    ax.text(p0[0]-1, p0[1]+0.5, p0[2]+1, r'$\hat n$', fontsize=15)

    plt.axis('off')
    plt.show()


#figure_1()
#figure_2()
#figure_3()
figure_4()
