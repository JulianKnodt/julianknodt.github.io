# Shape Intersections

I derived some general equations for the intersection of some shapes in graphics!

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
A cone, parametrizd by it's apex(C), base radius(r), length(l), and axis direction(V).

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

From this, we can derive that the intersection of cone can be computed by solving the quadratic
equation with terms
```
a = D^T Q D
b = 2 L^T Q D
c = L^T Q L
```
Where Q can be precomputed based on the characteristics of the cone.
More on Q later.

---

## Cylinder
A cylinder parametrized by it's center(C), base radius(r), length(l), and axis direction(V).

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

From this, we can derive that the intersection of cone can be computed by solving the quadratic
equation with terms
```
a = D^T Q D
b = 2 L^T Q D
c = L^T Q L - r*r
```
This has a striking resemblance to that of a cone, except for Q missing the k constant, and the
additional parameter `r*r` in c.


TODO add bit about spectral decomposition of q and efficient computation of a, b and c.

