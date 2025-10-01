# Overview
During the summer after freshman year in high school, I went to some math program in NYU, which essentially was solving math-team-like questions. I thought I was good at math until I joined that program. One thing though always stuck with me, which was:

**Using two integers n and m, we can generate any right triangles by the following ...**

And that was all I remembered. I did not know how we got there, but I was fascinated by the concept. During my adult life, I remember it had maybe something to do with $n+m, n-m, 2m+1$ or some sort of combination. 

After starting this repository, once this thought came again I decided it's time to figure it out. After a graduate math degree and work experience, surely now I can figure it out.

---
*I will approach this derivation as my thinking process was on paper, so one can see the intuition behind all the moves*
---

# $A^2 + B^2 = C^2$

$A, B, C$ are all integers. So, maybe we can break these down into some smaller integers, $n, m$. The beauty of this is we can set A and B to be whatever we want in terms of $n,m$ and then solve for C. 

Let's start with something simple: $A = (n+m)^2$

Let's also then try $B = (n-m)^2$

What I immediately see is that the middle terms of both expansions will cancel out:

$$
\begin{align}
    A^2 + B^2 &= (n+m)^2 + (n-m)^2 \\
              &= (n^2 + 2nm + m^2) + (n^2 - 2nm + m^2) \\
              &= 2n^2 + 2m^2 \\
          C^2 &= 2(n^2 + m^2) \\
          C   &= \sqrt{2(n^2 + m^2)} \\
\end{align}$$

Now, that didn't work because we have to pick an $n, m$ such that $2(n^2 + m^2)$ is a perfect square. That isn't easy or quick.

---
Let's try something else. The intuition behind what to pick comes from realizing we can write:

$$B^2 = C^2 - A^2 = (C-A)(C+A)$$

This means we want to pick $A, C$ such that both $C-A$ and $C+A$ have some neat cancelations, and together produce a perfect square.

----
 What if instead of $B = (n-m)^2$, we have $C = (n-m)^2$?

$$
\begin{align}
    A^2 + B^2 &= C^2 \\
          B^2 &= C^2 - A^2 \\
              &= (n-m)^2 - (n+m)^2 \\
              &= (n-m - (n+m))(n-m + (n+m)) \\
              &= (-2m)(2n) \\
              &= -4mn \\
\end{align}
$$

Well I already see my mistake. I can't have a negative number for $B^2$. Of course, we know that $C>A$, so $C=(n+m), A=(n-m)$.

So let's switch the two:

$$
\begin{align}
    A^2 + B^2 &= C^2 \\
          B^2 &= C^2 - A^2 \\
              &= (n+m)^2 - (n-m)^2 \\
              &= (n+m - (n-m))(n+m + (n-m)) \\
              &= (2m)(2n) \\
              &= 4mn \\
          B   &= 2\sqrt{mn} \\
\end{align}
$$

Okay, that's nice. Now we just have to pick $n, m$ such that $mn$ is a perfect square. But this becomes a challenge once we want to work with high $n,m$ values. If we were to use this,
we would have to:

1. Pick an $n, m$ and write their product, $nm$.
2. Factor $nm$ into its prime factors, and hope we can get $(something)^2$
3. Iterate until we find a perfect square.

I was just about to settle on this, but I know when I was in NYU it was much simpler than that. Thinking more on this, I keep remembering that we are free to chose whatever we want for $n, m$ and $A, C$.

Why don't we just set: 

$$ m \rightarrow m^2 $$
$$ n \rightarrow n^2 $$

again this is just a change of variables. We are able to do this since $n, m$ are arbitrary integers. It's the same as saying:

$$ m = x^2 $$
$$ n = y^2 $$

where we introduced two new variables $x, y$. But to keep it simple, we just rename them back to $n, m$.

So, if we do this, we have:

$$ B = 2\sqrt{(n^2)(m^2)} = 2nm $$
$$ A = n^2 - m^2 $$
$$ C = n^2 + m^2 $$

And there we have it. We can generate any right triangle using two integers $n, m$ such that $n>m>0$:

$$ \boxed{A = n^2 - m^2, B = 2nm, C = n^2 + m^2} $$

---
After deriving this, I looked it up and found out this is called "Pythagorean triples".
---

I am curious about the implications of this in computer algorithmic settings. Given a triple, can we efficiently search for an n,m? Or can we use this to do faster computations regarding squares? Any other ideas?