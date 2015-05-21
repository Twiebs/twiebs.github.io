---
layout: post
title: Moving to Jekyll and Github Pages
tags:
    - Jekyll
    - Github
---

![JekyllLogoImage](/images/jekyll-logo.png)

I've decided to migrate my blog (that had one post) from Wordpress, to Jekyll, hosted with Github pages.  This configuration is much better and who knows, i might even start using it...  This is mostly a test post but if your intrested in starting with Jekyll here are some installation tips and tools to help get you started.

## Setting Up Jekyll
Fork Jekyll now.  Especialy if your a windows user.  It will provide a good starting point even if you plan on writing everything yourself. I encoutered a lot of friction attempting to use jekyll with windows; starting from a working project helps locating the source your problems.  I had diffucult esspecialy with syntax highlighting, but as you will see in a moment that has been resolved.  If your running windows i recomend taking a look at [this](http://jekyll-windows.juthilo.com/3-syntax-highlighting/).

## Writing posts and previewing changes
If you are creating a fork of Jekyll now the first thing you should do is setup Jekyll on your computer to make use of the live previewing tools.  I am using [Atom](https://atom.io/), to write my posts and fire up my edditing enviroment with the following python script.  Since i dual boot my desktop with Arch Linux and run it exclusivley on my desktop the script accomodates both the windows and linux platform and provides the same functionality.

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
