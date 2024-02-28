# FBX is Fuck

FBX is a standard format for 3D models, which contains animation, texture, and geometry
information. These are details of why it's absolutely fuck.


I've been working with the FBX format recently, and not just passing it in & out out of Unreal
Engine or Unity, but actually changing the output Assimp which is an open-source import/export
library. Assimp, as the name (ASSet IMPort Library), is mostly concerned with importing the
thing, so when it tries to export an FBX, it currently poops out a moderately similar version.
That's no fault of the Assimp devs, as FBX is FUCK. There's no open-spec for Assimp, so it's a
lot of trial and error to figure out exactly what is correct.

As an example, FBX is structured as a directed graph of nodes, with each node connected by a "connection"
to another node. Now, each node has its own "version", which seems to be number starting from 100,
and it seems that by changing the "version" of a single node, how it behaves when imported can differ.
Note that this is NOT a global version for the entire FBX, but a version FOR EACH NODE. Within the same
FBX file, you can have multiple nodes of the same thing all with different versions. Microsoft's
shaking in their boots thinking about backwards compatibility needed to maintain this system.

On top of that, each FBX node comes with a number of fields which are just constant. I now live
with the knowledge that there's just a bunch of useless strings in tons of games that is now
uselessly occupying space on everyone's PC and in my brain. On top of that, most enums in FBX
are just strings, so who knows what possible options there are for each value. Nevermind that
some keys are misspelled, like `acuracy` or `indexes`, they're just icing on the cake.

The most fuck thing about FBX is that they have an official FBX file explorer from Autodesk
which created FBX, and some models that load in Maya (also from Autodesk) don't in the official
explorer. Fuck! It doesn't even say why it won't load, and only says `File is Corrupted`!
Presumably because you haven't paid the Autodesk tax like all the people who use Maya and 3DS
Max, and are trying to circumvent their monopoly on the FBX IO. Another mind-blowing thing
is that some brilliant people at Blender went to good effort to reverse-engineer the FBX spec,
and implement their own loader. Then these same people went and slapped a GPL license on top of
it! Power to them, but to me it feels like this license fucks over other OSS stuff that want to
consume FBX without using the official SDK. With FBX's versioning as well, they can just do a
version bump, add a bunch of keys which are just 🖕 (kidding, FBX doesn't support UTF encoding),
and break all that hard work of reverse-engineering done to figure out the layout. I know that
there's been towards USD (Universal Scene Description) for new models, and I have yet to actually
check that out. But I'm sure it has own flaws too, and maybe later in the future, I can have a
USD is Fuck post as well.
