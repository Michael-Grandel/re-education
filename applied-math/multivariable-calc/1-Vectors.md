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
\boxed{\vec a \cdot \vec b = \sum_ia_ib_i} \rightarrow a_xb_x + a_yb_y + a_zb_z 
$$

## Cosine application
Let's use vectors and attempt a simple problem from trig. In doing this, we will see the dot product appear, and some neat relationship with the angle between two vectors.

![Cosine rule for finding triangle leg length](/data/applied-math/multivariable-calc/Figure_2.png)

Using trigonometry (we can also derive this in the 'other' section), know this relationship between the length of the triangle's legs:

$$ 
|\vec c|^2 = |\vec a|^2 + |\vec b|^2 - 2|\vec a| |\vec b|\cos\theta 
$$

----
To make notation simpler, let's take note that every vector can be written as a scalar times the unit vector in that direction:

$$ \vec a = a\vec u_a $$

Therefore, using $|\vec u|=1$, we can write the length as:

$$ |\vec a| = |a\vec u_a| = a |\vec u_a| = a $$

To make it clear, when referring to the length, the notation I will use is:

$$
  |\vec a| = a
$$

----
So we have:

$$ 
c^2 = a^2 + b^2 - 2ab\cos\theta
$$

So the question here is: Since we know both vectors, a and b, which have magnitudal and directional information, can we figure out the angle between them? In theory, we should be able to.

$$ \cos\theta = \frac{c^2 - a^2 - b^2}{-2ab} $$

We can evaluate c in terms of a and b, since we know:

$$ \vec c = \vec b - \vec a $$

We can re-write (derived below): 

$$ c^2 = (\vec b - \vec a) \cdot (\vec b - \vec a) $$

---

$$
\begin{align}
\vec a \cdot \vec b &= \sum_ia_ib_i \\
\vec a \cdot \vec a &= \sum_ia_ia_i \\
                    &= \sum_ia_i^2  \\
                    &= |a|^2
\end{align}
$$

Meaning, the dot product between a vector and itself is the sum of it's components, squared. Which is the same thing as the length of the vector, squared.

---
One more thing to derive is what (if any) is the distributive property of vectors

$$
\begin{align}
\vec a \cdot (\vec b \pm \vec c) &= \sum_i a_i(b_i\pm c_i) \\
                                 &= \sum_i a_i b_i \pm a_i c_i \\
                                 &= \sum_i a_i b_i \pm \sum_i a_i c_i \\
                                 &= \vec a \cdot \vec b \pm \vec a \cdot \vec c 
\end{align}
$$

Thus, it distributes just like in scalar multiplication

---

Putting these together, we can now express:

$$ c^2 = b^2 + a^2 - 2 \vec a \cdot \vec b $$

$$ \therefore \cos \theta = \frac{-2\vec a \cdot \vec b}{-2ab}$$

$$ \boxed{\cos \theta = \frac{\vec a \cdot \vec b}{ab}} $$

## Direction Vector (Unit Vector)
We can use this now to discover a fast way to compute unit vectors, which we will see also is the direction.

If we replace $\vec b$ with the axes (x-axis, y-axis, z-axis) $\rightarrow(\hat i, \hat j, \hat k)$, we will be measuring the cosine of the angle between vector a and the axis. In other words, this is the direction of $\vec a$.

$$
\cos \alpha =\frac{\vec a \cdot \hat i}{a|\hat i|} = \frac{\vec a \cdot \hat i}{a} = \vec u_a \cdot \hat i = u_a^i\hat i
$$

Note that last step is possible because $\hat i = <1, 0 , 0, >$, so the dot product is easy to compute. Doing similar with the other two axes, we end up with:

$$
\begin{align}
\cos\alpha &= u_a^i \hat i \\
\cos\beta  &= u_a^j \hat j \\
\cos\gamma &= u_a^k \hat k \\
\therefore \vec u_a &= u_a^i \hat i + u_a^j \hat j + u_a^k \hat k \\
\vec u_a &= \boxed{<\cos\alpha, \cos\beta, \cos \gamma>}
\end{align}
$$

So, the unit vector of a vector is simply the cosine of all the angles between the respective axes.

## Projection Application
We can now derive another common interpretation of what a dot product is. If we take what we just derived for cosine, we write the dot product as:

$$ \vec a \cdot \vec b = ab \cos \theta $$

If we take a look at this image, we can piece somethings together:

![projection and dot product](/data/applied-math/multivariable-calc/Figure_3.png)

$$ \begin{align}
a\cos \theta &= |\text{proj}_{b} \vec{a}|  \\
             &= \frac{\vec a \cdot \vec b}{b} \\
             &= \vec a \cdot \vec u_b
\end{align}
$$

$$ \boxed{|\text{proj}_{b} \vec{a}| = \vec a \cdot \vec u_b} $$

That's the first thing: the magnitude projection of vector a onto vector b, is the dot product of vector a and the **unit vector of b**.

This leads to the second thing, the actual projection vector is thus:

$$ 
\boxed{\overrightarrow{\text{proj}_{b}a} = \frac{\vec a \cdot \vec b}{b} \vec u_b = \left ( \frac{\vec a \cdot \vec b}{b^2} \right ) \vec b}
$$

And finlly the third thing: the dot product of vector a and vector b, is the projection of a times the scale of b. _In my 'boosting' concept, it is how much of a is boosting b, in the direction of b._

$$ \boxed{\vec a \cdot \vec b = b(a\cos \theta) = b|\text{ proj}_{b} \vec{a}|} $$
