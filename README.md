# Purpose
Super File Galaxy is a project I started to make Super Mario Galaxy 1/2 file management easier by representing the file
structure with human-readable Python classes, removing the need for complex file I/O. The file data is represented using
specifically typed class attributes that can either be initialized with a file or used to write a new file. This can be
helpful for analyzing, creating, or changing existing files, or it can be used as a package that other SMG software can
run off of. On top of the easier file management, it also provides detailed warnings and errors when a file is 
malformed.

# Setup
If the repository is cloned, these steps are necessary for ensuring the project dependencies are properly set up:
1. If a virtual environment has not been created, run the following command in the terminal located at the root 
   directory: \
    ``python -m venv .venv``

2. Activate the virtual environment:
    * Windows: \
            ``.venv\Scripts\activate``
    * Mac/Linux: \
            ``source .venv/bin/activate``

3. Install the project package into the environment: \
    ``pip install -e .``
