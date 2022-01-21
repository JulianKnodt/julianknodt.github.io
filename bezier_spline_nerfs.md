# Bezier Spline Dynamic NeRF

- Jan. 21, 2021

![mutant bezier spline nerf](images/mutant.gif)

This is a brief introduction to a simple idea for modifying Neural Radiance Fields (NeRFs) to handle
dynamic scenes in a classical format, so that they can be reconstructed instantly. I will
move the explanation of Neural Radiance Fields to the bottom, so please skip
[there](#Neural-Radiance-Fields) if you would like to know what they are before jumping into the
main points.

## Problem:

Neural Radiance Fields are interested in reconstructing functions `f(x,y,z) -> density,
f(x,y,z,viewing direction) -> rgb`.
By shooting a light ray through some volume, we can see where the ray would terminate after
accumulating enough density, allowing us to model complex objects which may have transparency,
and view dependent effects. Dynamic NeRF extends this to a more general function:
`f(x,y,z,time) -> density, f(x,y,z,time,view) -> rgb`. One of the original [Dynamic NeRF
papers](https://arxiv.org/abs/2011.13961) decomposes these functions into two parts:
`delta(x,y,z,time) -> dx, dy, dz, f(x+dx, y+dy, z+dz) -> density, f(..., view) -> rgb`. In this paper,
`delta` is modelled as a neural net, more specifically as an MLP.

There has been a trend in static scenes which have no time component to develop classical
models, which can be trained much more quickly by pruning aggressively in sparse voxel grids,
and have many fewer parameters which are guaranteed to be local. Since the delta was modelled as
a neural net, it forces the classical model to be slow to optimize since it has to be evaluated
at every point.

## New Classical Model:

In order to alleviate this problem, instead of modelling `delta` as an MLP, we can instead model
it with bezier splines, which would permit for it to be extended to a classical model.  [Bezier
splines](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) are a specific form of polynomial
function, defined by a set of points. The reason they immediately come to mind as a tool is
because they are common in animation and games already, so there are both many tools for using
them, and people are already aware of a lot of their properties. The best resource I've found
for them is this [primer](https://pomax.github.io/bezierinfo/). It would do it injustice for me
to explain it here, so I would read the introduction of that to get a better idea of what Bezier
splines are.

We can extend NeRF to use them in a classical manner, for example, at each point on a voxel
grid, we would maintain a set of bezier points, and a time `t`, we trilinearly interpolate
within the voxel, and compute a bezier spline for a specific point. At the same time, we can
also modify `delta` to output a set of control points: `delta(x,y,z,t) -> N x 3 control
points`, still using the prior MLP framework. This is much simpler to implement, and given that
I'm a single individual working on this project it is much more plausible to do. I'd hope it
makes the classical model more efficient as well, since it also forces `delta` to learn a
continuous interpolation over time.

The source code for my implementation is
[here](https://github.com/JulianKnodt/nerf_atlas/blob/4e4c8e9911a283c76ce632178f9c989bfccb6eb8/src/nerf.py#L911),
and contains a basic implementation of using splines for recovering dynamic scenes. I'm not
great at tuning hyperparameters, but as is it seems to work alright for its task.

A paper describing the whole thing is still in progress, but I think this is a useful
optimization so I wanted to write a brief bit about it since I'm shit at making diagrams so it
may be a while before I put up anything on ArXiv.

## Note:

More than anything else, on its own it is not that useful of an optimization. But I certainly
think combining it with classical models will be very powerful for fast dynamic neural
graphics. I hope that this work gets incorporated elsewhere.

## Neural Radiance Fields Summary {#Neural-Radiance-Fields}

TODO just copy and paste this from somewhere else
