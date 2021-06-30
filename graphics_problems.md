# Problems in Machine Learning & Graphics

The field of machine learning & graphics seems to be relatively new, with the explosion of
[Neural Radience Fields](https://www.matthewtancik.com/nerf) for view-synthesis, for
reconstructing 3D models from a set of 2D images. Previously, there wasn't a ton of potential to
go from easily gathered 2D images to 3D spaces, and this seems to bridge the gap, enabling a
large number of 3D applications. Here, I hope to clarify what these possibilities for graphics
and machine learning are, since they might not come to mind immediately.
<!-- Also a good way to document for myself! -->

## What are Graphics & Machine Learning?

Before digging into what ML&G (MLG?) does, it's useful to understand what each subfield is.

Machine learning, in essence, is the field of function approximation. Given a series of inputs
and outputs, find some function that approximately maps from the inputs to the outputs, and can
be used for previously unseen inputs to approximate some outputs. Usually, these functions
aren't known, such as learning which images have a picture of a hot dog or not.

Graphics is concerned with taking a description of a 3D scene, and producing 2D outputs.
Generally, the 3D scene can be considered to be the object in the scene, the textures, lighting,
and sometimes animations. This field has existed since the inception of computers, and thus
there are many different approaches to rendering and modeling, which have different levels of
expressivity, efficiency and realism. A lot of work has been put into physically-based
raytracing, which seeks to accurately reproduce realistic looking images, while not being
impractical to run.

The intersection of these two fields is inverse rendering. Given some differentiable method for
taking a 3D model to an image, perform regression on the output from rendering against some
other image in order to learn some parameters of the model. Ideally, if we take a picture of a
cat, we should be able to recreate a 3D scene with the cat in the same position as in the
picture. This is done by learning the geometry of the cat, the texture and color of its fur, and
some features of the lighting as well. Of course, this currently isn't possible but hopefully
will be in the future.

---

So what interesting things are feasibly tackled by graphics in combination with machine
learning?

- Given 1 image, output a 3D scene:

I think is one of the hardest problems to do, because it requires prior information about the
world, including how objects usually look like, how lighting interacts with objects, and what
kind of textures are feasible. I think this is probably possible, just needs a lot of
computational resources for each of these components.

- Given N > 1 images, output a 3D scene:

This is the problem that Neural Radiance Fields solve. Given a lot of views of a single, static
object, it is easy to reconstruct it now. The hard part now is reconstructing scenes where
objects are moving, there are effects only in some frames such as flames, or the pictures are
non-continuous, such as a tourist photos of monuments. There are approaches to solve these
issues, but there is no consensus on what the best approach is, and they've only been tested on
a limited number of datasets.

- Given text, output a 3D scene:

This is a stretch goal, I think it'd be really awesome to provide a text description of an
object or scene, and be able to create a 3D scene from it. Up to now, there's been a lot of
interesting work in generating 2D images from text. If we can generate an image from text, and a
3D scene from an image, then this should be plausible. I don't think it's necessary to have an
intermediate step, so I think that this is actually possible but will require a lot of
computational resources.

- Given two 3D models, crate an interpolation between them.

This is an artistic idea, but if you're given a cat and a dog, what is halfway between them?
Or, if a person is in two different poses, how do they smoothly move between them? This is just
a fun side idea.

- Given N images, create a renderer which outputs any object in the style of those images.

This one is a bit more abstract. Imagine if you have a bunch of images from a video game, such
as Wind Waker (which was well-known for it's cartoon art style). If we take a bunch of images
from those games, then we want to be able to render any 3D model in the style of those images.
This probably isn't too hard to implement, but I think it has fun applications.
