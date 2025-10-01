# Overview
As I begin my setup for multivariate calc, the first derivation is the distance formula in n-dimensions. For that, I would start with extending from 1D to 2D, and just say we all know it.

But, in the spirit of deep mathematical understanding, let's derive this classic. Which, at the end of the day, is also deriving the **pythygorean theorem**.

This will also help me kick off the source code in the dev folder, which will be used to generate images for future derivations.

# Distance formula in 2D
Let's start with two points in 2D space, and call them A (x1, y1) and B (x2, y2).

![Image of a line](/data/applied-math/other/Figure_1.png)

We can project these points down to the x and y axis, and draw a right triangle. The hypotenuse of this triangle is the distance between the two points, which we will call $z$.

[Image generated with code in dev/ folder]

Now to find a relationship between x and y, to get z. In otherwords, we want to find $f$ such that:

$$z = f(x, y)$$

To find such a relationship, we can extend the projected x-leg to form another right triangle. The reason we are doing this is because we will have geometric relationships between the triangles, where angles are equal to each other. 

This means the triangles are dilations of each other and allow us to form equations. This can also be derived, but it is a fundemental concept in geometry that I will skip. (If you scale a triangle, the angles remain the same, and all the sides increase by the same scale).

[Image generated with code in dev/ folder]

There are 3 triangles here, the big one, and the two smaller ones, all with the same 3 angles. So, the proportion of the sides across each of them are the same:

$$ 
\frac{\text{side across } \alpha_{\bigtriangleup1}}{\text{side across }\alpha_{\bigtriangleup2}} = \frac{\text{side across } \beta_{\bigtriangleup1}}{\text{side across } \beta_{\bigtriangleup2}}
$$

$$
\frac{x}{y} = \frac{y}{x_e} \\
\frac{z}{x} = \frac{x+x_e}{z}
$$

So now we can solve for $z$ in terms of $x$ and $y$: 

$$ xx_e = y^2 \\
z^2 = x^2 + xx_e$$
$$ \boxed{z^2 = x^2 + y^2} $$