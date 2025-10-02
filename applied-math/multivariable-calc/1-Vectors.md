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

```math
\begin{align}
D_{\mathbb{R}^n} &= \text{Distance in } \mathbb{R}^n \\
D_{\mathbb{R}^{n+1}}^2 &= \underbrace{D_{\mathbb{R}^n}^2}_{\text{projection}}+ \underbrace{(A_{n+1}-B_{n+1})^2}_{\text{new vertical}}
\end{align}
```

# Sphere
So, just like in 2D, a sphere is the set of points that are equidistant from a point; all points a radius $r$ away from the center.

The equation of a **hollow** sphere is, centered at $(x_0, y_0, z_0)$ is the distance formula:

$$ \boxed{c = r^2 = (x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} $$

A hypersphere, which is the same thing in n-dimensions:

$$ c = r^2 = \sum_{i=1}^n (x_i - x_{i0})^2 $$

A **solid** sphere would be all points that are within the radius; an inequality.

$$ c \geq (x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2 $$

# Vectors
Fundemental knowledge that I won't go over:

1. What a vector is
2. How they add and scale
3. Notation
4. Length and unit Vectors

## Dot product
This value has less of a derivation and more of an explanation. This is because there is a pattern in math that comes up alot when working with 2+ vectors and running computations.
This pattern was assigned the 'dot product', and through many common applications there are different interpretations. My intepretation of it is:

> The dot product of two vectors $\vec a$ and $\vec b$ is a measure of the total "boosting" between $\vec a$ and $\vec b$; 

* If two vectors are in the same direction, their dot product would be the product of their length _(magnitude/length/boost)_
* If two vectors are perpendicular, then there is no 'boost' in the other's direction, so their dot product is 0.

$$ 
\boxed{\vec a \cdot \vec b = \sum_ia_ib_i} \newline
\rightarrow a_xb_x + a_yb_y + a_zb_z 
$$

