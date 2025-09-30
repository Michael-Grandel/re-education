# Overview
During a trip for a wedding in Honduras, myself and two friends were left at a cafe in the jungle why we waited for other friends to arrive. During this time, somehow the question came up:

<b> "How can you tell a number is divisible by 3?" </b>

We already knew the answer, but then I extended it by asking, "Do you know why?" 

And so, the derivation begins.

## Writing a 3 digit number algebraically
Lets start with a 3 digit number:

$$ ABC $$

If we use 745, in this case $A = 7, B = 4, C = 5$. Lets write this number algebraically.

$$ ABC = 100A + 10B + C $$

So now, if we want to check if this number is divisible by 3, we can check if $100A + 10B + C$ is divisible by 3. <b> But what does it "really" mean, algebraically, if a number is divisible by 3? </b>

---
Well, it means we can write a number, $N$, as a product of 3 and another integer number:

$$ N = 3n \mid n \in \mathbb{Z}$$

For example, $6 = 3(2), 90 = 3(30)$, but $7 = 3(\frac{7}{3})$, hence 7 is not divisible by 3.

---
Thus, if $ABC$ were to be divisible by 3, then we can write:

$$ ABC = 3n \mid n \in \mathbb{Z} $$
$$ 
\begin{align}
n &= \frac{100A + 10B + C}{3} \\
  &= \left (33A + \frac{A}{3} \right ) + \left (3B + \frac{B}{3} \right ) + \frac{C}{3} \\
  &= 33A + 3B + \left (\frac{A + B + C}{3} \right )
\end{align}
$$

Now let's talk about what happened. If think about this logically, we don't care about "what is the number divided by 3", but "if it is divisible by 3".
The way I see it is looking at objects, like coins/change, and trying to divide it into 3 even groups. What really matters in the end is if we have any remainer.
I don't care how many coins are in the group, just if there is any remaider.

So in the lets look at 100A: if we just divide that by 3, the only remainder is A/3. 
The same goes for 10B, the only remainder is B/3.

If we want to look at this more algebraically, we know in step 3 that $33A + 3B$ is already an integer, because $\lbrace 33, A, 3, B \rbrace$ are all integers, and the product/sum of integers is an integer.

So the only part that determines if $n$ is an integer is the last part, $\frac{A + B + C}{3}$. 

**Thus, if $A + B + C$ (the sum of the digits) is divisible by 3, then the whole number $ABC$ is divisible by 3.**


## Full derivation: extending this to n-digit numbers
We only derived the rule for a 3 digit number. But does this whole true for any number?
Let's extend this to an n-digit number. <i> (Below technically is an n+1 digit number, but that's just an 'm' digit number )
</i>

$$ x = 10^nx_n + 10^{n-1}x_{n-1} + ... + 10^2x_2 + 10^1x_1 + 10^0x_0 $$
$$ x = \sum_{i=0}^{n} 10^i x_i \mid x_i \in \mathbb{Z} $$

Now, we want to check if $x$ is divisible by 3. So we can write:

$$ 
\begin{align}
x &= 3k \mid k \in \mathbb{Z} \\
k &= \sum_{i=0}^{n} \frac{10^i}{3} x_i \\
\end{align}
$$

---
$10^i$ is every power of 10, so $\lbrace 1, 10, 100, 1000, ... \rbrace$.
We can re-write all of these as: $\lbrace 1, 9 + 1, 99 + 1, 999 + 1, ... \rbrace$. 

Why am I writing it like this? Because when we divide by 3, every power of 10 is written as a number divisible by 3, plus 1. 

So we always go to some 99999 like number, which is divisble by 3, and our remainder is always 1. But, to be mathematically correct, we need to write this algebraically.

More precisely, we can write:

$$ 10^i = 9(10^{i-1}) + 9 (10^{i-2}) + ... + 9(10^0) + 1 $$
$$ 10^i = \left ( 9 \sum_{j=0}^{i-1} 10^j \right ) + 1 $$

---
Lets plug this back into our equation for k:

$$
\begin{align}
k &= \sum_{i=0}^{n} \frac{10^i}{3} x_i \\
  &= \sum_{i=0}^{n} \frac{\left ( 9 \sum_{j=0}^{i-1} 10^j \right ) + 1}{3} x_i \\
  &= 3 \sum_{i=0}^{n}\sum_{j=0}^{i-1} 10^jx_i + \sum_{i=0}^{n} \frac{x_i}{3} \\
  &= N +  \sum_{i=0}^{n} \frac{x_i}{3} \mid N \in \mathbb{Z} \\
\end{align}
$$

Now, we can see that $N$ is an integer, because it is a sum/product of integers. So the only part that determines if $k$ is an integer is the last part, $\sum_{i=0}^{n} \frac{x_i}{3}$. 

**Thus, if $\sum_{i=0}^{n} x_i$ (the sum of the digits) is divisible by 3, then the whole number $x$ is divisible by 3.**

---
---
## Other divisibility rules
Using the same logic, we can derive other divisibility rules. For example, an easy one is:

**Why do we always look to see if last digit is even, to see if a number is divisible by 2?**

Let's start with an n-digit number again:

$$ x = \sum_{i=0}^{n} 10^i x_i \mid x_i \in \mathbb{Z} $$

We want to check if $x$ is divisible by 2. So let's skip the mathematical formality and just divide by 2:

$$ \frac{x}{2} = \sum_{i=0}^{n} \frac{10^i}{2} x_i $$

Now more clearer than for 3, powers of 10 are all divisible by 2, except for $10^0 = 1$.

$$ 
\begin{align}
    \frac{x}{2} &= \sum_{i=0}^{n} \frac{(5\cdot 2)^i}{2} x_i \\
                &= \sum_{i=1}^{n} 5^i 2^{i-1} x_i + \frac{x_0}{2}\\
                &= N + \frac{x_0}{2} \mid N \in \mathbb{Z} \\
\end{align} 
$$

**Hence, a number is divisble by 2 if the last digit, $x_0$, is divisble by 2 (even).**

---
Using this, we can discover new divisibility rules for everything. The goal is to learn to process, and then it can be applied to any problem.