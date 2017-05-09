---
layout: page
title: Projects
permalink: /projects/
---

# LLVM based Compiler Frontend for Custom Language

A simple compiler frontend that targets LLVM.  Custom language
is very close to C with a very minimalistic syntax for simplicty.

[GitHub](https://github.com/Twiebs/compiler02)


# TJW-OS: Kernel + Basic Operating System

This is a very simple forever WIP kernel and operating system implemented in C and x86_64 ASM.
Only written for long mode capiable machines.  Handles multi-processor startup, has a WIP ehci
drive and ext2 filesystem

# Venom: Game Engine and tools

### Noteable Implemented Features:

- Multi-threaded task scheduling and execution
- OpenGL Renderer
  - Deferred Renderer
  - Ambient Occlusion
- Entity Management System
- Asset Management System
  - Asset Hot-reloading
- Procedural Generation Tools

# C Site Generator

This project is used to generated the website that you are currently viewing.
It is a small single file library that exposes a data driven C interface for generating HTML.
The system becomes incredibly flexible and powerfull when used with compositing functions together
to generate webpages.  This data driven interface allows html generation based on any arbitrary data source.

### Features
- Data driven immediate mode interface
- Standard HTML tag generation 
- Incremental Markdown parser 
	- Custom markdown procedure call syntax
- C/C++ syntax highlighting

You can check out an example of how this tool is used by taking a look at the source code used for this
website.

[This blogs source code](http://github.com/twiebs)
[site_generator.h](http://github.com/twiebs/single-file-libraries/site_generator.h)

---

## Other Miscellaneous Projects

[Ludum Dare 34 Entry](http://ludumdare.com/compo/ludum-dare-34/?action=preview&uid=5078)
[Ludum Dare 34 Code](https://github.com/Twiebs/LD34)

[Ludum Dare 33 Entry](http://ludumdare.com/compo/ludum-dare-33/?action=preview&uid=50789)
[Ludum Dare 33 Code](https://github.com/Twiebs/LD33/)