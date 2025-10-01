# Distance Formula
![Line in 3D](/data/applied-math/multivariable-calc/Figure_1.png)

What is the distance between A and B? The image above shows projections of lines onto different planes, which allows us to use 2D distance formula to derive the 3D distance one.

$$
\begin{align}
\overline{AB}^2 &= \overline{AC}^2 + \overline{BC}^2 \\
                &= (\overline{AD}^2 + \overline{CD}^2) +\overline{BC}^2
\end{align}
$$

So, its just the sum of squares of all the projections. In otherwords, if $d$ is the distance:

$$
\overline{AD}^2 = \Delta x^2, \overline{CD}^2 = \Delta y^2, \overline{BC}^2 = \Delta z^2
$$

$$
\boxed{
    d^2 = \Delta x^2 + \Delta y^2 + \Delta z^2
}
$$

One can extend this to $n$ dimensions, by using induction. The distance of the next (n+1) dimension just involves the distnace of projection in $n$ dimensions and the new vertical.

$$
\begin{align}
D_{\mathbb{R}^n} &= \text{Distance in } \mathbb{R}^n \\
D_{\mathbb{R}^{n+1}}^2 &= \underbrace{D_{\mathbb{R}^n}^2}_{projection} + \underbrace{(A_{n+1}-B_{n+1})^2}_{new vertical}
\end{align}
$$
