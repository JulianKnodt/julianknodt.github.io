# An Intro to Raytracing/Pathtracing

- 28th-January-2023

This is a short guide to raytracing, which outlines the problem raytracing is used to solve,
how raytracing goes about solving that problem, and different subcomponents of raytracing.

It should not be considered a definitive guide, but should give an intuitive understanding of
what raytracing does.

## Problem: Rendering 3D Objects Realistically

The primary purpose of raytracing is to render 3D objects as we would see them in real life.
This stands in contrast to something like rasterization, which projects objects onto the screen,
and then color selection is done in screen space without considering complex lighting. The
difference is primarily due to efficiency, since rasterization requires fewer intersection checks,
instead only requiring a comparison of distance of object from the camera.

## Understanding how we see in real life

To understand how raytracing works, we first have to understand how people see and how
cameras work. Animals see through light that enters the eye, hitting receptors. These receptors
act similar to pixels, and react to light, which has a color and intensity. We treat light as
particles which travel linearly, and is emitted from some source, such as a lightbulb.
Light particles can bounce off 0 or more surfaces, until it hits a receptor, or its intensity is
no longer visible, as the intensity drops with the square of the distance traveled.
Receptors accumulate light incoming from all directions, and the sum of light is the final color
we see.

##### A rough plausible algorithm

From this rough description, we can devise an outline of an algorithm:

Given a number of 3D objects, which include descriptions of surface materials and how they
reflect light, an eye position and viewing direction, and lights:

1. From each light, emit some number of rays from each light source in arbitrary directions.
2. For each light ray, compute the intersecting objects.
3. Repeat 2 until each ray reaches the eye, or continues to bounce beyond a distance limit.
4. Sum up light at each pixel, and return all pixels as final image.

##### Revising the rough algorithm

While the above approach is how real life works, computationally it is infeasible to compute. Some
rays may take indefinitely long to reach the eye, and many pixels have no light reach them at
all if we are unlucky.

To ensure that light reaches every pixel of the eye, we can invert the problem. From
each pixel in the eye, we cast a ray to detect the amount of light on some surface the ray
intersects.

Our new approach is as follows:

1. For each pixel in the eye, cast rays in the viewing direction.
2. Find the first surface of intersection, and compute the accumulated light hitting that point.
3. Multiply the amount of light hitting the surface by the percent that is reflected in the
  direction of the eye. This is defined by the material of the surface.
4. Sum up the accumulated light for all rays for each pixel, and return the resulting image.

From this algorithm, we now see that we have fixed issues from the previous approach, where we
are guaranteed to terminate, and that each pixel will now be illuminated.

We now have a new problem though, which is that we have something arbitrarily complex in the
middle of our algorithm: how do we compute the amount of light hitting a surface? This is the
same problem as computing the amount of light hitting the eye, so we can see that raycasting can
be framed recursively. To
make sure that our algorithm does not infinitely recurse, we can instead *approximate* the
amount of light hitting the surface.

For example, a simple approach is to cast a ray from the surface to each light, and we compute
the intensity of light if it is not occluded by each surface It might be useful as an exercise
to think about why we can do this for a surface, but not for the original camera).
This is called *direct raytracing*, and it paths which contain 1 bounce off a surface.

### How does direct raytracing perform?

Direct raytracing is effective and simple, but it's approximation is visually noticeable. It's
primary issue is that it leads to *hard shadows*. Hard shadows are when there is a visible pixel
line where an object is illuminated, and suddenly becomes completely dark. This is because
effects from light bouncing on multiple objects is not captured which can reach areas that are
occluded is not captured. We can extend direct raytracing to include multiple paths, and
including multiple paths is known as *pathtracing*. There are many varieties of
pathtracing, which can include a fixed number of bounces, or an arbitrary number.

### Approximating bounces in a pathtracer

To compute paths, we have to perform many different kinds of sampling. For example, at
each surface, the direction of the bounce is defined as a set of probabilities on the hemisphere
of the surface, as a given function of the material. For some number of paths, we randomly
select a direction on the hemisphere, and shoot a ray in that direction. Ax another, we may be
interested in sampling from a light which is defined continuously along a shape (think of a
rectangular ceiling light), and we have to decide where on this light we want to sample. Again,
we want to sample from some probability distribution. By performing enough samples, we
approximate the complete contribution of all inputs.

This is known as [Monte Carlo Sampling](https://en.wikipedia.org/wiki/Monte_Carlo_method).

##### Inefficiencies of Monte Carlo Sampling

One issue with Monte Carlo sampling is that we may be sampling a light ray which has an
extremely small illumination. For example, a 5 bounce path may have very small contribution to
the final color and computing each bounce is computationally expensive. To prevent
unnecessary contribution, we can increase the probability that we stop bouncing as the
contribution becomes smaller. To be precise, with some probability `q`, which is a function of
the current contribution, we stop computing along the path. If we do continue to compute values
along the path, they are reweighted by the probability `1/(1-q)`. This is done primarily to
reduce the number of useless expensive computations, and is known as *Russian Roulette*.

### Things not in this introduction

This intro does not cover how surface materials work, glossing over it and defining it as some
function which dictates how much light bounces from one direction into a different direction.
There are many different implementations of different materials, and a comprehensive overview
can be found in PBRT, or other guides. If you see the term BSDF, that refers to descriptions of
these materials.

## References

These references are more complete, and will help you get a full understanding of the details of
raytracing.

- [PBRT](https://pbrt.org/)
- [Raytracing in a weekend](https://raytracing.github.io/books/RayTracingInOneWeekend.html)
- [Scratchapixel](https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/how-does-it-work.html)
