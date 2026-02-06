# A Proposal for Simplifying Dot-Product Attention

A common operation in LLMs is dot-product attention, Softmax(QK^T)V.

Ultimately, this operation is O(N^2) with the size of Q and K, as that produces the pairwise
dot-product between each row of Q and K. This is one of the most costly components of LLM, as
the size of Q and K correspond to what parts of an input should "pay attention" to other parts.

I will say I am not up-to-date with all the recent approaches for improving the efficiency
either at inference or during training. There's some things like
[Big-Bird](https://arxiv.org/abs/2007.14062), which change the architecture to be sparse, or
purely system optimizations such as [Flash
Attention](https://github.com/Dao-AILab/flash-attention). Both
approaches are needed for the most efficient implementation.

Here, I want to briefly describe a small mathematical optimization that I haven't heard of
(although could be in use right now). I'm unable to test it myself, since I'm less familiar with the
architecture of LLMs and am unsure what an appropriate test would be. That may mean this change
is not meaningful, but I thought it'd be good to document it nonetheless.

For the change itself, it's rather straightforward, it is converting the dot product into a
distance, which can be approximated more straightforwardly.

```
dist(a,b)^2 = dot(a,a) + dot(b,b) - 2 * dot(a,b)
dot(a,b) = 1/2 (dot(a, a) + dot(b,b) - dist(a,b)^2)
```

This formula converts the dot product into 3 different components. The first two terms are
linear, and reflect the importance of `a` and `b`. These terms would be fast to compute.
The third term is the computationally expensive pairwise distance term, which is again O(N^2).
Here, though, rather than the dot-product which gives us the positive relation between two
terms, distance now corresponds to negative relationship, where the distance between `a` and `b`
is negatively correlated with the final attention.

The reformulation thus has a few benefits. First, the attention between two items now depends on
their importance, so it may be possible to discount some terms entirely. I suspect that most
items will have non-neglible importance though. Instead, another benefit comes from the distance
term. Here, we can replace direct computation with an approximate nearest neighbors, giving an
algorithmic speed-up of O(log n). Of course, whether this is actually faster than a matrix
multiply depends on the implementation, as nearest neighbor checks must be done for many
high-dimensional vectors, and many algorithms for doing so will eventually fall back from O(log
n) to O(n) due to the curse of dimensionality.

Since I am not actually implementing these, I thought I'd put it in writing and share it so that
for someone of interest it may be of use.
