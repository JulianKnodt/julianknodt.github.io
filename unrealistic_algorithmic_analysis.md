# Unrealistic Algorithmic Analysis

Time/Space complexity analysis is the standard method for understanding how long an algorithm
might take to run. This approach is based on the fundamental idea that primitive operations(such
as an array access, a pointer indirection, or floating point operation, are all weighted
equally. In addition, there is also the assumption that the average case is most important, and
thus the pain of a costly operation can be offset by a ton of cheap operations as long as the
operations are dominated by the cheap operations.

For most people, these analyses are sufficient, in that the code most people are dealing with is
sufficiently abstract from the machine where a single high-level operation is a mix of many
smalller operations, so what appears to be a fundamental operation, such as `3 + 3`, might be a
combination of type-checking, and invokation of other functions. In these cases, algorithmic
complexity is sufficient, as operations can be treated as pretty much equal.

The real issue is when it comes to low-level languages like C++ or C, where there are massive
differences between these operations. Of most note is memory accesses, where pointer
chasing(following a series of pointers) are grossly inefficient compared to linear traversal of
arrays. Essentially this boils down to most people just tossing out algorithmic analysis because
they are not great models for figuring out how long things take, and just throwing together
random algorithms until they find one that is fast enough for their use case.

Thus, these traditional algorithmic complexity models are not used, because they are god-awful at
predicting performance in real life, as opposed to in the brain of some computer scientist. Of
course, the computer scientist will say, "this is good enough, it's a model and doesn't need to
be extremely precise", to which you would hopefully respond: "What?! That's outrageous, you're
making something useless and you're fine with it?!". Maybe it's true that it's fine that models
can't be exactly like reality, but they sure as hell could be closer than what they currently
are.

# Proposal to better model run-time

Of course, I'd just be a dick if I insulted the people who make such models without proposing
some meaningful change that would make it more meaningful. So what could actually make these
models more meaningful? What's missing from the current models is a differentiation between
fundamental operations. For example, floating point operations should not be lumped in with
array accesses. Once there's a clear distinction between operations, we can think about how to
use this more precise descriptor to determine the cost on a given "computer model".

A "computer model" is some abstract computing environment, which could for example be a run-time,
a distributed environment, or a machine description. One pragmatic way to take a "computer
model" and compute a more realistic expectation of runtime is to define a set of normalized weights
over a set of defined operations. For example, floating point operations might be expected to
take 5 cycles, whereas a pointer access might take 100, so we would weight FP operations as
1/20th of a pointer access, and normalize all these weights to sum to 1. These can then be
multiplied by the corresponding operations for a given algorithm in order to produce a more
realistic estimate of run-time.

This idea is actually a generalization of the original, in that if we use equal weights for all
operations, we will end up with the total operations divided by the total kinds of operations.

Of course, this is not a panacea for the issue of practicality. Notably, memory accesses have a
complex relationship. Array accesses are not always faster, in that it depends if we do a bunch
of linear accesses in a row such that the data can be prefetched and the cost offset. But, we
can estimate an expected cost of array accesses and the like to get closer to the goal of
practicality. In order to increase accuracy further it stands to reason that after looking at
some possible descriptions of algorithms using this model, it will be more clear what can be
added to make this even more pragmatic.

---

At some point, I might add a description of an algorithm using this concept, but currently I am too
lazy to do so. Cheers.


