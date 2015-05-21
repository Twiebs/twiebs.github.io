---
layout: post
title: Visualizing Noise
tags:
    - Raptor
    - Game Development
    - C++
    - Procedural Generation
    - Engine
---

Planned Features:
Web Previewer with Emscripten

The type of noise can be set in the visualizer.  The types are classess that inherit from a noise interface.  Their Eval methods are overriden but noise processing functions such as fbm or ridgged noise are implemented in the base noise class.  This allows for all noise implementors to use these functions and provider the results as seen in the webapp.  

This is the header for the noise classess that are used in the vizualizer.

Noise.h
{% highlight cpp %}

{% endhighlight %}
