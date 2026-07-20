# Textures to Vert Colors

<center>
<video controls width="720">
  <source src="/videos/textures_to_vert_colors_ff.mp4" type="video/mp4" />
</video>
</center>

## Designing a coaster:

Using the tools in this paper, it's straightforward to design a coaster from an image:

What you'll need:
- An image for converting into a coaster
  - The image shouldn't be too complex.
- [Blender](https://www.blender.org/)
  - With basic knowledge of how to edit meshes :).
  - Tutorials [1](https://www.youtube.com/watch?v=DHv9PSPikpM),
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
