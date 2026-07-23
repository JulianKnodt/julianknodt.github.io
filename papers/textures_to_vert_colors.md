# Textures to Vert Colors

Julian Knodt and Seung-Hwan Baek

![POSTECH CGLab](https://cg.postech.ac.kr/wp-content/uploads/2024/04/cropped-logo.png)

[Code](https://github.com/JulianKnodt/texture_to_vert_colors)

[Paper](https://dl.acm.org/doi/10.1145/3804451)

Questions? Email me at julianknodt@gmail.com.

## Abstract:

<small>
3D artists blend geometry and texture to craft objects and their appearance, using both geometric and image processing tools. Yet, it is difficult for geometry processing to account for textures in the standard UV with texture maps representation. When textures are represented as vertex colors though, we show texture-aware geometry processing becomes straightforward. Unfortunately, most textured meshes are represented with UV parameterizations, so in practice most geometry processing tools simply ignore texture. This scarcity of vertex colors meshes is remedied using a new remeshing approach that hoists textures to vertex colors through per-triangle remeshing, while preserving input appearance. This new remeshing takes meshes with UVs and texture maps and generates vertex color meshes, which are then used to show how vertex colors can be incorporated into geometry processing through texture-aware modifications to multiple applications. Specifically, we test texture-aware geometry processing on surface segmentation, Tutte parameterizations, surface texture processing algorithms such as edge-detection, and vector field operations with the texture gradient. For each application, texture information produces different and in some sense improved results as compared to geometry-only algorithms, or image processing algorithms performed in UV space.
</small>

## Fast-Forward:

<center>
<video controls width="720">
  <source src="/videos/textures_to_vert_colors_ff.mp4" type="video/mp4" />
</video>
</center>

This work converts textured meshes into meshes of vertex colors by projecting pixels onto triangle faces in 2D, and resampling in 3D.
The use of vertex color meshes is then  demonstrated in applications including clustering, texture aware UV parameterization, view-independent texture edge detection, and quad  remeshing following a texture’s gradient.

## Designing a coaster:

Using the tools in this paper, it's straightforward to design a coaster from an image:

What you'll need:
- An image for converting into a coaster
  - The image shouldn't be too complex.
- [Blender](https://www.blender.org/)
  - With basic knowledge of how to edit meshes. Some tutorials are linked below.
- [This Project's Code](https://github.com/JulianKnodt/texture_to_vert_colors)
- [Rust for compilation](https://github.com/rust-lang/rust)
- [uv for scripts](https://docs.astral.sh/uv/)

1. Change to the source code directory for the project:
`cd texture_to_vert_colors`

2. Create a vertex color mesh with:
```
cargo run --release -- -i data/plane.obj -d <PATH TO YOUR IMAGE> \
  --target-tri-num -o vert_color_mesh.ply
```

3. Split the mesh into charts with separate color. You may have to tweak the number of pieces
you break it into, with `-t`. `clusters.ply` has the output images clusters
```
cargo run --release -- -i vert_color_mesh.ply -o clustered_mesh.ply -t 20 \
  -c clusters.ply
```

4. This step requires a little bit of artistry. Open the mesh in blender. You can now select
regions by going into edit mode, selecting a vertex in a region, and then selecting all [linked
vertices](https://www.youtube.com/watch?v=9yxzi-95pXk). Clusters can then
[be extruded](https://www.youtube.com/watch?v=DHv9PSPikpM) to show the design.
Background colors can also be deleted.

5. Rotate the mesh 90 degrees so that it's flat with the ground, and [add a
cylinder](https://www.youtube.com/watch?v=dDW16bFlA7w).
Then export the mesh as either a PLY or OBJ, and you have something ready for 3D printing!

Here's an example done with the Hong Kong flag:

<center>
  <img src="/images/example_coaster.png" width="400" alt="Example Coaster">
</center>
