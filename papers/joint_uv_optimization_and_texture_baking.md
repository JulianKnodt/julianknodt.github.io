# Joint UV Optimization and Texture Baking

- [Slides](https://docs.google.com/presentation/d/1EC4kKl7hSoI7ivLxErMdiaVL5cGd4Z8b/edit#slide=id.p1)
- [Paper](https://dl.acm.org/doi/10.1145/3617683)
- [Models from Paper](https://github.com/JulianKnodt/texture_baking_supplementary)

TODO: I still need to stick images here, they'll make it a lot easier to understand.

##### Preface

This is a blog post that gives an intuitive description for the paper *Joint UV Optimization and
Texture Baking*. Hopefully, you'll find it easily understandable, especially as compared to
papers, which often are not intended to be readable to people who don't already know a lot.

### What is texture baking?

When making games, artists will often produce meshes that are way too big to use in a game. For
example, they can contain millions of triangles, which would make any game dev cry when trying
to render them in real time. Thus, game devs and artists rely on tools to produce simpler
models, which can then be actually rendered in the game. One example of this is mesh reduction,
which progressively reduces the number of edges. When decimating massive meshes to relatively
small ones, i.e. 1e7 to 1e3 faces, this kind of reduction can introduce errors, so it isn't
usable in every case. Instead, there's alternate approaches, which include reconstructing the
mesh from the ground-up to match the original shape. Unfortunately, such approaches cannot
preserve the original texture of the mesh.

When remeshing causes the original texture to be lost, we want to be able to port the original
texture to the new mesh. There are existing tools to do this, such as
[Marmoset](https://marmoset.co/posts/toolbag-baking-tutorial/). These tools often require some
amount of parameter tuning, which can be a time-sink, and may produce artifacts if not tuned
correctly.

In a completely different vein, there's a new way to perform texture reconstruction in the form
of differentiable rendering. This allows a model to be rendered from many views, and a texture
to be reconstructed from each of the 2D images.

We try to make differentiable rendering work for texture baking!

#### Running into problems:

Initially, we thought it'd work right off the bat, with no changes. In reality though, of course
that didn't work. I spent about 2 weeks trying to figure out why it had blurry output. Finally,
I reached the conclusion that because the geometry in the input and output were different, the
texture became blurry, because the texture was being copied from multiple of the original
model's texels, as seen from different viewing directions, into a single pixel on the simplified geometry.

This is actually cited in the [paper](https://github.com/NVlabs/nvdiffmodeling) on
differentiable rendering, but, they brush it off, identifying that as optimization of vertices
continues, this will become less and less of a problem, or you can just more vertices. For us
though, we cannot introduce more vertices as it will increase the cost of rendering in game, so
there's always going to be some error. So instead we have to figure out some way to get around
the error, without adding higher resolution.

### Getting around different geometry

One way to frame that differently is that the texel on the simplified geometry is actually very
close to the original, but shifted a few pixels over based on viewing direction. To fix this, we
actually just want to change the UV based on the viewing direction. To do that, there's a bunch
of stuff for forward rendering, which uses a depth map to shift the UV. These kinds of functions
are called parallax mappings, because they emulate depth parallax. This works pretty well,
but for optimization it can be a bit difficult, as they all bake a number of assumptions,
including that the surface is flat. Instead, we optimize a function based off
Spherical Harmonics, which unlike previous parallax. This seems to work pretty well during
optimization. Sometimes though, especially when the surfaces are completely different, there are
artifacts that look like cracks that appear in the texture.

### Removing parallax for downstream use

Now that this parallax map has been used to generate a texture map, we actually need to remove
it, unless the application supports it. To do so, we think of the parallax mapping function
as `f(UV, view direction)`. To make the texture no longer dependent on the viewing direction, we
make it fixed: `f(UV, face's normal)`. Because we express the view direction in the local
normal, bitangent, tangent basis of the face, this is equal to `f(UV, [0,0,1])`. Then we can
just resample into a new texture, and that can be used in downstream applications.

### Poor UV of small resolution textures

Another thing we notice is that UV for small textures may actually be quite bad. This is because
UV optimization generally is done without thought for number of contained pixels, or the content
of the texture. Thus, some triangles are not given enough pixels, and thus the final texture
looks bad. To fix this, we optimize the UV coordinates of the pixels, based on the triangle
rendering loss. We perform a traditional per-chart bijective optimization, and weigh the energy
of each chart with the image loss. We also perform edge-edge collision checks with checked step
size to prevent charts from overlapping with each other, and use a
[smooth energy](https://github.com/ipc-sim/IPC) to ensure that as triangles approach they "push"
each other away. We find this approach to be robustly improve quality of the final rendering.

### Geometry optimization

Another thing we find is that the previous work's laplacian regularization on mesh geometry may
work if the mesh is extremely dense, but will degrade quality when the mesh is
coarse. Instead, we only deform vertices in the direction of the vertex normal, and find that
this leads to better matching of geometry.

TODO: make this flow better and add a conclusion
