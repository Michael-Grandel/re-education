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

### The dot product of two vectors $\vec a$ and $\vec b$ is a measure of the total "boosting" between $\vec a$ and $\vec b$ 

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

# Cross Product: Find the perpendicular vector
Another quantity that commonly arrises is defined as the cross product. I believe the intuition of creating this came from the following question:

### Given two vectors, $\vec a, \vec b$ what is the perpendicular vector to them?

Using all our equations for the dot product, we can quickly derive that perpendicular vectors has a dot product of 0. Let's say our perpendicular vector is $\vec n$, then:

$$ \vec a \cdot \vec n = \vec b \cdot \vec n = 0 $$

$$ 
\begin{align}
    a_in_i + a_jn_j + a_kn_k &= 0 \\
    b_in_i + b_jn_j + b_kn_k &= 0 \\
   \rightarrow b_k(a_in_i + a_jn_j) - a_k(b_in_i + b_jn_j) &= 0 \\
   \underbrace{(a_i b_k - a_k b_i)}_p n_i + \underbrace{(a_j b_k - a_k b_j)}_q n_j &= 0 \\
   pn_i + qn_j &= 0
\end{align}
$$

One solution is: $n_i = q, n_j = -p$. Which we can then plug in and solve for $n_k$.


$$ 
\begin{align}
n_i &= a_jb_k - a_kb_j \\
n_j &= a_kb_i - a_ib_k  \\
n_k &= a_ib_j - a_jb_i
\end{align}
$$

### This is the cross product: $\vec n = \vec a \mathsf{x} \vec b$
There are several ways to remember this. My prefered way is:

1. If we want $n_i$, that means we have a combo of $j, k$ for $\vec a$ and $\vec b$.
2. It's always a difference between 2 terms
3. The terms go in the order of $i \rightarrow j \rightarrow k \rightarrow i \rightarrow ... $


Example: cross product: $ \vec z = \vec x \mathsf{x} \vec y $ 
(I will start with the 2nd element)

1. Let's start with $z_j$, so that means we will have two terms subtracted, starting with $x_k$ and then $x_i$. The y-terms will be the component that x is **not**.

$$ z_j = x_ky_i - x_iy_k $$

2. Then let's go to $z_i$, so that means we will have $x_j$ and then $x_k$:

$$ z_i = x_jy_k - x_ky_j $$

3. The last one is $z_k$, so we will go from $i \rightarrow j$:

$$ z_k = x_iy_j - x_jy_i $$

---

This is simple for 3 terms, but there is a way to also do it for n-dimensions. We won't do it here, but the approach is the same:

1. We will have n-1 dot products all equal to 0
2. We will have n-1 factors next to each $n_i$ term
3. We will be able to set each factor to $p_i$
4. Then we can come up with values for each $n_i$ as a product of all the _**other**_ $p_i$ terms and some extra numerical factor. 

For example, in the case of 4 dimensions we will have:

$$ p n_i + q n_j + zn_k = 0 $$

One solution is: $n_i = qz, n_j = pz, n_k = -2pq$, and then we can solve for $n_l$, the 4th term.

---

So now, let's be curious. We explored what $ \vec a \cdot \vec a$ is, but now what is:

$$\vec a \mathsf{x}  \vec a = ? $$

Well logically, we there are infinite vectors that are perpendicular to a singular vector... so the answer is either 0 or infinity I'd suppose. 

If we plug into the equations we just derived, all the two terms being subtracted are equal, so they cancel.

$$ \boxed {\vec a \mathsf{x}  \vec a = 0} $$

Next, what is the length of the perpendicular vector?

$$ | \vec a \mathsf{x} \vec b | = ? $$

Let's plug it all in:

$$ 
\begin {align}
| \vec a \mathsf{x} \vec b | ^ 2 &= (\vec a \mathsf{X} \vec b) \cdot (\vec a \mathsf{X} \vec b ) \\
&=  (a_jb_k - a_kb_j)^2 + (a_kb_i - a_ib_k)^2 + (a_ib_j - a_jb_i)^2 \\
&= a_j^2b_k^2 + a_k^2b_j^2 +a_k^2b_i^2 + a_i^2b_k^2 + a_i^2b_j^2 + a_j^2b_i^2 - 2(a_ja_kb_kb_j + a_ka_ib_ib_k + a_ia_jb_jb_i) \\
&= a_i^2(b_j^2 + b_k^2) + a_j^2(b_i^2 + b_k^2) + a_k^2(b_i^2 + b_j^2) - 2(a_ja_kb_kb_j + a_ka_ib_ib_k + a_ia_jb_jb_i) \\
&+ a_i^2b_i^2 - a_i^2b_i^2 + a_j^2b_j^2 - a_j^2b_j^2 + a_k^2b_k^2 - a_k^2b_k^2 \\
&= (a_i^2 + a_j^2 + a_k^2)(b_i^2 + b_j^2 + b_k^2) - (a_i^2b_i^2 + a_j^2b_j^2 + a_k^2b_k^2 + 2(a_ja_kb_kb_j + a_ka_ib_ib_k + a_ia_jb_jb_i)) \\
&= |\vec a|^2|\vec b|^2 - ((a_ib_i + a_jb_j)^2 + a_k^2b_k^2 + 2(a_ja_kb_kb_j + a_ka_ib_ib_k)) \\
&= |\vec a|^2|\vec b|^2 - (a_ib_i + a_jb_j + a_kb_k)^2 \\
&= |\vec a|^2|\vec b|^2 - (\vec a \cdot \vec b)^2 \\
&= a^2b^2 - a^2b^2 \cos^2 \theta \leftarrow \text{(remember notation)} \\
&= a^2b^2(1-\cos^2 \theta) \\
&= a^2b^2\sin^2\theta \\
\therefore |\vec a \mathsf{x} \vec b| &= ab\sin \theta
\end {align}
$$

So, if we have the angle then we can use the final result. Otherwise, we can use the dot product from the result 4-times previous.

$$ \boxed{|\vec a \mathsf{x} \vec b| = ab\sin \theta = \sqrt{a^2b^2-(\vec a \cdot \vec b )^2}} $$

---
Let's derive the distributive properties, and then have one big summary of everything we learned about vectors.

$$ \vec a \mathsf{x} (\vec b + \vec c) = ? $$

Let's just look at one component and see what happens:

$$
?_i = a_j(b_k+c_k) - a_k(b_j + c_j) = (a_jb_k - a_kb_j) + (a_jc_k - a_kc_j) 
$$

So we can see this same pattern for the other terms, leading to:

$$\vec a \mathsf{x} (\vec b + \vec c) =  \vec a \mathsf{x} \vec b + \vec a \mathsf{x} \vec c$$

Next, in doing something similar, we can see the order of the cross product **matters**:

$$ (\vec b + \vec c) \mathsf{x} \vec a =  \vec b \mathsf{x} \vec a + \vec c \mathsf{x} \vec a \neq \vec a \mathsf{x} (\vec b + \vec c)$$

Next:

$$\vec a \cdot (\vec b \mathsf{x} \vec c) = ? $$

$$ = a_ib_jc_k-a_ib_kc_j + a_jb_kc_i - a_jb_ic_k +a_kb_ic_j - a_kb_jc_i $$

$$ = c_i(a_jb_k-a_kb_j) + c_j(a_kb_i-a_ib_k) + c_k(a_ib_j-a_jb_i) $$

$$ = (\vec a \mathsf{x} \vec b) \cdot \vec c $$

Finally... this is a long one:

$$ \vec a \mathsf{x} (\vec b \mathsf{x} \vec c) = ? $$

$$ 
\begin{align}
&= \vec a \mathsf{x} 
        \begin{bmatrix}
            b_jc_k - b_kc_j \\
            b_kc_i - b_ic_k  \\
            b_ic_j - b_jc_i
        \end{bmatrix} \\
&=      \begin{bmatrix}
            a_j(b_ic_j - b_jc_i) - a_k(b_kc_i - b_ic_k) \\
            a_k(b_jc_k - b_kc_j) - a_i(b_ic_j - b_jc_i) \\
            a_i(b_kc_i - b_ic_k) - a_j(b_jc_k - b_kc_j)
        \end{bmatrix} \\
&=      \begin{bmatrix}
            (a_jc_j+a_kc_k)b_i - (a_jb_j + a_kb_k)c_i \\
            (a_ic_i+a_kc_k)b_j - (a_ib_i + a_kb_k)c_j \\
            (a_ic_i+a_jc_j)b_k - (a_ib_i + a_jb_j)c_k 
        \end{bmatrix} \\
&=      \begin{bmatrix}
            (a_ic_i + a_jc_j+a_kc_k)b_i - (a_ib_i + a_jb_j + a_kb_k)c_i \\
            (a_ic_i+ a_jc_j + a_kc_k)b_j - (a_ib_i + a_jb_j + a_kb_k)c_j \\
            (a_ic_i+a_jc_j + a_kc_k)b_k - (a_ib_i + a_jb_j + a_kb_k)c_k 
        \end{bmatrix} \\
&= (\vec a \cdot \vec c) \vec b - (\vec a \cdot \vec b) \vec c
\end {align} 
$$

In that last step, notice how we can always add 0. So, for example, in the first component I added $a_ib_ic_i - a_ib_ic_i = 0$, and this nicely distributed into both parentheses. I did that because I wanted to try making the first term look like a dot product, which luckily made the second term also one. That's not luck, it's the beauty of math!

So let's summarize all our rules below:

# Summary
### Basic rules:
$$ 
\boxed{
    \begin{align*}
    \vec a \cdot \vec b &= \sum_ia_ib_i       &      \vec a \cdot \vec b &= ab \cos \theta     &  \vec a \cdot \vec a &= a^2\\
    \vec a \mathsf{x} \vec b &= \begin{bmatrix}
                                    a_jb_k - a_kb_j \\
                                    a_kb_i - a_ib_k  \\
                                    a_ib_j - a_jb_i
                                \end{bmatrix} &     |\vec a \mathsf{x} \vec b| &= ab\sin \theta & \vec a \mathsf{x} \vec a &= 0 
    \end{align*}
}
$$

### Distributive rules:
$$
\boxed{
\begin{align}
\vec a \cdot (\vec b \pm \vec c) &= \vec a \cdot \vec b \pm \vec a \cdot \vec c \\
\vec a \mathsf{x} (\vec b \pm \vec c) &=  \vec a \mathsf{x} \vec b \pm \vec a \mathsf{x} \vec c \\ 
\vec a \cdot (\vec b \mathsf{x} \vec c) &= (\vec a \mathsf{x} \vec b) \cdot \vec c \\
\vec a \mathsf{x} (\vec b \mathsf{x} \vec c) &= (\vec a \cdot \vec c) \vec b - (\vec a \cdot \vec b) \vec c
\end{align}
}
$$

** Order matters for cross product

### Other
1. If you don't have the angle between vectors, you can also find the length of the cross product as: 

$$ |\vec a \mathsf{x} \vec b| =\sqrt{a^2b^2-(\vec a \cdot \vec b )^2} $$


2. The dot product between $a$ and $b$ can also be viewed as the projection of $a$ along $b$

$$ 
\overrightarrow{\text{proj}_{b}a} = \frac{\vec a \cdot \vec b}{b} \vec u_b = \left ( \frac{\vec a \cdot \vec b}{b^2} \right ) \vec b
$$

$$
 |\overrightarrow{\text{proj}_{b}a}| = \vec a \cdot \vec u_b
$$

### Distance Formula (between a, b)

$$ \boxed{ d^2_n = \sum_i^n(a_i-b_i)^2 } $$

### Hyper sphere

$$
\boxed{
\begin{align}
    \text{Hollow: } r^2 &= \sum_i^n(x_i-x^0_i)^2 \\
    \text{Solid: } r^2 &\geq \sum_i^n(x_i-x^0_i)^2
\end{align}
}
$$
