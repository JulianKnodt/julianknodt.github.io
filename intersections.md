# Shape Intersections

I derived some general equations for the intersection of some shapes in graphics!
They might be useful if rendering conics is compute bound, and this might be an interesting
approach to try to see if it reduces compute, but otherwise, I just found it fun to think about
and implement.

I've not found them elsewhere, so I thought I would write them down here.
Why would you actually use these as opposed other methods? Hopefully they provide efficiency
gains in that a recurring parameter in these equations, Q(the characteristic matrix of the
conic), is not actually dependent on the
input ray, but is only dependent on the conic. Thus, we can pre-compute Q, which is an expensive
operation. In addition, we only need to use Q for a limited number of matrix-vector
multiply. 3 to be specific. Since this is the case, we can pack together the 3 vectors so that
we only need to do one 3x3,3x3 multiply, rather than perform them serially. This can better
utilize efficient matrix multiplication vectorization. We also avoid any cosine or sine
operations, or dealing with any angles because trigonometry is hard and slow.

In addition, we hope to show that it is possible that the intersection of an arbitrary conic can
be defined as a quadratic form with a linear and constant term. Notably, we see that the cone
and cylinder have very similar Q matrices, but there is an additional term in the equation of a
cylinder.

## Cone
A cone, parameterized by it's apex(C), base radius(r), length(l), and axis direction(V).

The general parametric equation of a point(P) on such a cone would be:
```
let h = (P-C)^T(V) in
(P-C)^T(P-C) = h * h * (1 + (r*r)/(l*l));
```

The operations to simplify it are as follows:

```
let h = (P-C)^T(V) in
(P-C)^T(P-C) = h * h * (1 + (r*r)/(l*l));

let k = (1 + (r*r)/(l*l)) in
(P-C)^T(P-C) = h * h * k;
-> (P-C)^T(P-C) = k*(P-C)^T(V) V^T(P-C);
-> (P-C)^T(P-C) - k*(P-C)^T (VV^T) (P-C) = 0;
-> (P-C)(I-kVV^T)(P-C) = 0;
```
At this point we would like to substitute the ray equation for P;
```
let R + tD = P in
(P-C)(I-kVV^T)(P-C) = 0;
-> (R+tD-C)(I-kVV^T)(R+tD-C) = 0;
let L = R-C in
(L+tD)(I-kVV^T)(L+tD) = 0;
let Q = I-kVV^T in
(L+tD)Q(L+tD) = 0;
L^T Q L + 2t L^T Q D + t^2 D^T Q D = 0;
```

From this, we can derive that the intersection of a ray with a cone can be computed by solving the quadratic
equation with terms
```
a = D^T Q D
b = 2 L^T Q D
c = L^T Q L
```
Where Q can be precomputed based on the characteristics of the cone, but more on Q later.
These equations can also be used to quickly compute the normal of the cone.

---

## Cylinder
A cylinder parameterized by it's center(C), base radius(r), length(l), and axis direction(V).

The general equation for a point(P) on such a cylinder would be:
```
(P-C)^T(P-C) = r*r + ((P-C)^T(V))^2
```

The operations to simplify it are as follows:
(We use a lot of the tricks we use above)
```
(P-C)^T(P-C) = r*r + ((P-C)^T(V))^2
-> (P-C)^T(P-C) = r*r + (P-C)^T(VV^T)(P-C)
-> (P-C)^T(I-VV^T)(P-C) - r*r = 0;
let Q = I-VV^T in
let R + tD = P in
let L = R - C in
(L+tD)^TQ(L+tD) - r*r = 0;
L^T Q L + 2t L^T Q D + t^2 D^T Q D - r*r = 0;
```

From this, we can derive that the intersection of a ray with a cylinder can be computed by solving the quadratic
equation with terms
```
a = D^T Q D
b = 2 L^T Q D
c = L^T Q L - r*r
```
This has a striking resemblance to that of a cone, except for Q missing the k constant, and the
additional parameter `r*r` in c.





Now the question is whether this is actually useful. I think the answer to this is, it depends.
For the most part, most modelling software will use just triangles to render things. If you are
trying to render conics, this might be useful. Unclear why you need to model conics at all
though(maybe thin lines for cylinders or something).

As for computational efficiency, it would appear we need to do at least 3 matrix-vector
multiplies and then 3 more vector-vector dot products in order to compute a, b, and c. If you
consider this expensive, we're still in luck(I found computing the matrix-vector products to be
somewhat expensive). Looking at the structure of `Q = I - kvv^T`,
taking k = 1 to be a special case for cones, we notice that `Q^T = Q`, From this alone, we
determine that we can diagonalize the matrix into `Q = V^T S V` for some diagonal matrix D and
some orthogonal matrix V. From this we can see that
```
a = D^T V^T S V D
b = 2 L^T V^T S V D
c = L^T V^T S V L
```
Now assume S is positive semi-definite(not sure if this is true in practice, I imagine it
probably always is or a counterexample would immediately appear). Then we can write `S = BB`,
where B is the elementwise square root of S(elementwise since S is diagonal). Now, we can
rewrite above to be
```
a = (B V D)^T(B V D)
b = 2 (B V D)^T(B V L)
c = (B V L)^T(B V L)
```
`(B V)` can be precomputed and is a function of the shape itself, so we do not count it in the
matrix multiplications. Thus, we only need 2 matrix vector multiplies and 3 vector-vector dot
products.


