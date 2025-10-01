import matplotlib.pyplot as plt

def plot_line(A:tuple, B:tuple, 
              point_label:tuple[str, str] = None, 
              line_label:str = None,
              a_alignment:tuple[str, str] = ('left', 'center'),
              b_alignment:tuple[str, str] = ('right', 'center'),
              l_alignment:tuple[str, str] = ('center', 'bottom'),
              style='k-'):
    """
    Plot a line segment between points A and B.
        params:
            A, B are points (x, y)
            point_label is the text to label both points ("A", "B")
            line_label is the text to label the line segment "d"
            alignment values are matplotlib alignments
    """

    x_values = [A[0], B[0]]
    y_values = [A[1], B[1]]
    plt.plot(x_values, y_values, style)

    if point_label:
        a_ha = a_alignment[0]
        a_va = a_alignment[1]
        b_ha = b_alignment[0]
        b_va = b_alignment[1]

        plt.text(A[0], A[1], point_label[0], fontsize=12, ha=a_ha, va=a_va)
        plt.text(B[0], B[1], point_label[1], fontsize=12, ha=b_ha, va=b_va)
    
    if line_label:
        l_ha = l_alignment[0]
        l_va = l_alignment[1]
        plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, line_label, fontsize=12, ha=l_ha, va=l_va)