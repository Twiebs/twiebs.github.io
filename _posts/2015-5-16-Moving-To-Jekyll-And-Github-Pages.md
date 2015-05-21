---
layout: post
title: Moving to Jekyll and Github Pages
tags:
    - Jekyll
    - Github
---

I've decided to move my blog(that had one post and was made a year ago) to
Github pages.  So far I really like the new setup who knows, I might actually start
using it...

This is mostly a test post but I am going to share some of the tools I'm using
to automate the editing process.

##Setting Up Jekyll
I followed Githubs guide for setting up Jekyll [here](https://help.github.com/articles/using-jekyll-with-pages/)
This allows for local previewing before making your changes live.

In order to simplify this process I created this very simple windows batch script
to first open [Atom](https://atom.io/), which I am using to edit my posts, then open
the default web-browser to the URL jekyll will be served to and then finally start
the jekyll server.

Recently i encountered issues with my computer and needed to do a fresh install.  I decided to try the Windows 10 Insider preview
I suspect some of the issues I am experiencing might have to do with windows 10

I encountered some difficulty enabling syntax highlighting with either rouge or pygments.

Mabye i should put something here...

{% highlight python linenos%}
__author__ = 'Torin Wiebelt'
# Simple Python Script for automating the jekyll post creating process
# Includes sytem calls for windows and linux

import platform
import subprocess

# Paramaters
jekyllWindowsDir = "D:/workspace/twiebs.github.io"
jekyllLinuxDir = "~/workspace/twiebs.github.io"

if platform.system() == "Linux":
    subprocess.call("cd " + jekyllLinuxDir, shell=True)
    subprocess.call("atom", shell=True)
    subprocess.call("xdg-open http://localhost:4000", shell=True)
    subprocess.call("bundle exec jekyll serve --drafts", shell=True)
elif platform.system() == "Windows":
    subprocess.call("cd " + jekyllWindowsDir, shell=True)
    subprocess.call("./atom", shell=True)
    subprocess.call("start http://localhost:4000", shell=True)
    subprocess.call("bundle exec jekyll serve --drafts", shell=True)
{% endhighlight %}

###Other good Resources
http://jekyll-windows.juthilo.com/3-syntax-highlighting/
