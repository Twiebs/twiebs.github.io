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
