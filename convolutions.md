# Convolutions

I've not found any notes on various convolution algorithms. I thought I would aggregate some
notes on them here.

Specifically, looking at the implementation of various discrete convolution algorithms.
Convolutions in 1D are of the form:
Discrete Convolve 1-D: (input: R^n, kernel: R^m) -> R^n
And can be generalized as
Discrete Convolve N-D: (input: R^[Int; N], kernel: R^[Int; M]) -> R^[Int; N]


#### Direct Implementation

Convolution can be implemented

```
convolve(input: [R; N], kernel: [R; M]) -> [R; N]:
  let out = [0; N];
  for i in 0..n {
    for j in 0..m {
      // assuming accesses out of bounds return 0
      out[i] += kernel[j] * input[i - j - M/2];
    }
  }
  return out
```
This takes time proportial to O(mn), as for each output element, we must iterate over every
element of the kernel.

#### Toeplitz Matrix

Conversion to Toeplitz matrix, H, by setting each column of the matrix to be `[0..h..0]`,
where the number of columns in H is equal to m and the number of leading 0s in each column is
equal to the column index. The convolution can then be computed by taking the product Hx.

If the matrix H is computed explicitly, it can be expensive as it of size O(m\*(m+n)). Notably
though, a Toeplitz matrix is just a view of a matrix and thus we can avoid explicitly computing
it.

This can be abstracted to a higher dimension N by creating an N+1 dimensional tensor with the
tensor tiled in a similar way, and then multiplying along the tiled dimension.


