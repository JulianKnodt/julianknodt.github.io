# Sparsity Patterns

I've been working on a sparse matrix format, and was thinking about how to sparsify a matrix.
There are a couple popular methods for incurring sparsity, such as magnitude based thresholding
on an individual element level, or at the row-level. Row-based thresholding is
often used because they allow for more efficient computations, because it means we can cut whole
rows from sparse vector multiplication.

One issue with this approach is that the rank of the matrix being sparsified will decrease. Even
if the immediate value from that row is low, it is possible that the small amplitude is magnified
significantly through further operations. Thus, we would like to retain something of that row,
even if it is smaller. In addition, even if a row might surpass the threshold, we might be
retaining a lot of insignificant elements. Thus, we want to find some metric that can make the
matrix as sparse as possible while retaining the rank of the matrix.

Thus, we would like to propose a different method for sparsifying matrices, based on the
N-Rooks problem.

###### Rook Sparsity

For each row and column, we would like to retain exactly one value, such that the sum of the
absolute values of the retained values is maximized. This will retain the rank of the original
matrix by retaining one value per rank as well as the nullity by retaining one value per column.
This is similar to the N-Rooks problem in that if we consider the matrix to be a massive
chessboard, and all the values retained to be rooks, none of the rooks would be able to attack
each other.


If we consider the initial matrix to represent a strongly-connected graph (every vertex is
connected to all other vertices), then we're finding a set of vertex-disjoing cycles that
cover all the vertices, while maximizing the sum of all the edge weights.
I strongly suspect this to be a NP-hard problem to compute, as it is the case that [similar
problems](http://www.immorlica.com/pubs/cyclecover.pdf) are NP-hard.

If this is merely for pre-processing some matrix, we might not actually care about
the proposed runtime of an algorithm, unless it would only complete after the heat-death of the
universe, as might be the case for a large enough dense matrix.

One way to make an efficient algorithm for this is to approximate a solution. For example, one
can force a matrix to be more sparse initially by retaining at least `k` values per row and
column, and then running a naive brute force search over the elements.

##### Variations

I can think of multiple possible variants, including retaining `k` elements per row and column
instead of just 1, This would improve the amount of information retained if a lot of elements
were similar in magnitude.

Another interesting idea might be to consider retaining at least one value per diagonal. This is more
similar to the N-Queens problem, as now we replace non-attacking rooks by non-attacking queens.
I'm not sure what benefit there is to this approach mathematically, as I can't find any reason
to retain elements along diagonals as I don't know of anything that is preserved by that. One
possibility though is that if we perform this at a block-level by considering sums of blocks
rather than sums of individual elements, we can recursively perform this algorithm by iterating
over the set of possible configurations for a low enough N.

That is, if we can divide the original matrix into some M by M blocks, where M << N, we can
retain one block per row by considering the sum within the block, and then perform the algorithm
recursively within each block. A naive approach would have M in \[5, 8\], so that we can
brute-force search through a small-number of permutations.

