---
layout: post
title: Procedural Multi-verse (Part 1) - Inhabited
---

This is my [Forever Project](http://jwb.io/20130122-the-joys-of-having-a-forever-project.html).  Its a "game" (with no gameplay... more like a simulation) that is set the multi-verse.  

I started working on a 2D version of a solar system generator by accient  while developing a top down shoot called Inhabited.  The projct was supposed to be a simple mobile twin stick shooter but it quickly esclated and i gave up trying to actualy make a shipable app.  I started working a lot on the procedural generation of its planets and solar systems.  The generator used the diamond square algorithim and OpenSimpelexNoise to generate a heightmap using points inside a circle.  Intervals of the heightmap were assigned a color value and produced results like this:

I first started a project a while back called Inhabited.  It was original supposed to be a simple two stick shooter for android but evolved into me procedurally generating solar systems and being able to traverse the terrain.  This was a 2D project that always seemed to be trying to emulate 3D.  At first i thought it would be cool to actually have the game take place in a 2D universe but i slowly began gravitating towards a 3D implementation.

I became really interested in procedural generation and space in general

I rewrote the solar system generator in Unity3D and got pretty similar results; however ,i used very different techniques to obtain them.

Most procedural universe generators are misnomers.  They procedurally generate content within our universe, not a universe itself.  With this project i plan on generating a "multi-verse" each universe having their own laws of physics.

To acomplish this i am also developing a game engine to go with it.  I never really plan on "finishing" this project.  Its my
