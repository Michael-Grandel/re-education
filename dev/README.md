# Developer Folder
This folder holds source code and data that is used for generating references (primarily images) in the markdown files. Keeping things here allows me to organize and easily have simple module import paths.

As I continue to need to plot and visualize certain concepts, I notice patterns and repeated usage of certain utilities, so the structure of code continuously changes. 

The sole intention of this code is to support this repository, so backwards compatibility is not considered; structure, usage, and design can drastically change per PR. This also is not a full python project with packages and __init__ files. It's intended to be easily transportable
by just executing the .py files in their respective directories.