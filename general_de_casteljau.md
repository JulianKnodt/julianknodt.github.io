# Vectorized multi-dimensional De-Casteljau's algorithm

Recently, I was interested in computing De-Casteljau's algorithm over a large number of
dimensions. Since De Casteljau's algorithm is separable, we can run it over each one
independently, but this may be slow, and could use a boost from vectorizing along some number of
dimensions.

Let's consider a numpy implementation of De Casteljau's algorithm:
```
def de_casteljau(coeffs, t:[0,1]):
  betas = coeffs
  m1t = 1 - t
  N = coeffs.shape[0]
  for i in range(1, N): betas[:1] * m1t + betas[1:] * t
  # should now only have 1 along the first dimension
  return betas[0]
```

This works fine along one dimension. Now, we can apply this in 2D by flattening along another
dimension:
```
surf_ctrl_pts = <input_source> # with dimensions: (# ctrl pts, # ctrl pts, K), for some K
ctrl_pts_1d = de_casteljau(surf_ctrl_pts, t0)
out = de_casteljau(ctrl_pts_1d, t1)
```

As we increase the number of dimensions arbitrarily, this becomes increasingly costly,
as we will have to compute De Casteljau's algo for the number of dimensions there are.
Instead, we can vectorize it by computing them all at the same time:

```
def de_casteljau(coeffs, t:[0,1]^K, dims=K):
  betas = coeffs
  m1t = 1 - t
  N = coeffs.shape[0]
  for i in range(1, N): betas[:1, :1, <up to K>] * m1t + betas[1:, 1:, <up to K>] * t
  # should now only have 1 along the first dimension
  return betas.squeeze()
```

The one change is that now we need to keep track of a tensor of the times in 0 to 1, and not
just each one individually. I did not show that this form was identical, and it may be worth
doing so, but I'm fairly convinced that this is correct.
