---
layout: page
title: Projects
permalink: /projects/
---

----------

# LLVM based Compiler Frontend for Custom Language

A simple compiler frontend that targets LLVM.  Custom language
is C like with a very minimalistic syntax for simplicty.

This is a screenshot of an example real-time software rasterizer wrriten in the language.  The
code that generated the following output can be found [here](https://github.com/Twiebs/compiler02/blob/master/examples/software_rasterizer.src)

![Screenshot Image]({{ site.url }}/images/software_rasterizer.png)
Here is the [GitHub Repository](https://github.com/Twiebs/compiler02) for the compiler

------

# Kernel + Basic Operating System

This is a very simple forever WIP kernel and operating system implemented in C and x86_64 ASM.
Only written for long mode capable machines.  Handles multi-processor startup, has a WIP ehci
drive and ext2 filesystem, basic ELF loading and execution

[GitHub Repository](https://github.com/Twiebs/tjw_kernel)

----

# Practice Tracking Tool

This is a tool to track programming research and practice topics.
It will have a scheduling feature that reschedules already completed
topics for review based on several metrics.

![Screenshot Image]({{ site.url }}/images/practice_tracking_tool.png)

[Github Repository](https://github.com/Twiebs/practice_tracking_tool)

---

# Game Engine and tools

This is a forever WIP Game Engine and set of acompaning tools.  Has a OpenGL
renderer with a deferred rendering pipeline with SSAO.  Asset managment system
with asynchronous loading and hot-loading of modified assets.  Basic GKJ collision
system.  Proceduraly generated infinate terrain.  

[GitHub](https://github.com/Twiebs/venom)

[A different incarnation](https://github.com/Twiebs/Raptor)

-----

# LLDB Based Debugging Frontend and custom linux debugger library

A basic attempt at creating a debugging frontend for LLDB.  Also has 
a simple custom debugging library for linux systems called libdb.

![Screenshot]({{ site.url }}/images/lldb_frontend.png)

[GitHub Repository](https://github.com/Twiebs/debugger)

---

# C Site Generator

This project is used to generate a different incarnation of this blog and portfolio using
a simple data driven interface for C to generate the HTML and javascript.  Supported emiiting
common HTML tags, a internal markdown parser html converter, very simple  internal C/C++ parser for syntax
highlighting. 


[site_generator.h](http://github.com/twiebs/site_generator/site_generator.h)

-----

# Basic Logic Gate Simulator

A very simple tool for creating basic logic gate diagrams

![Screenshot]({{ site.url }}/images/hardware_simulator.png)

[GitHub Repository](https://github.com/Twiebs/hardware_simulator)
