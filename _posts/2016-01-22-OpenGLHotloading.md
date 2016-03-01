---
layout : post
title : Hotloading OpenGL functions with C preprocessor metaprograming
---

One of the important features that I wanted when creating this new iteration of my game engine
Was the ablity to hotload code while the engine is still running.  I wanted this system to be as maximaly flexiable
as possible.  I really wanted to be able to hotload code that contained OpenGL functions.  This is how i accomplished
OpenGL function hotloading in the Venom game engine.

#C Preprocessor Metaprograming

The problem is that when the dll containing the game code is realoaded after compilation functions that
exist in the engine's executable will not be avaible to it.  OpenGL functions are loaded in the engine
using the same system that the game code uses to obtain them.

The opengl procedures are defined in the file opengl_procedures.h
This is a small example of what that file looks like

```
...

_(PFNGLGENTEXTURESPROC, glGenTextures)
_(PFNGLTEXSTORAGE2DPROC, glTexStorage2D)
_(PFNGLTEXSTORAGE3DPROC, glTexStorage3D)
_(PFNGLTEXIMAGE2DPROC, glTexImage2D)
_(PFNGLTEXIMAGE3DPROC, glTexImage3D)
_(PFNGLTEXSUBIMAGE2DPROC, glTexSubImage2D)
_(PFNGLTEXSUBIMAGE3DPROC, glTexSubImage3D)

...
```

Using the C preprocessor allows the defintions of the OpenGL functions to be pasted in locations where
they are realevant

```


```
