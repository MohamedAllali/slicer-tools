# String marker tool

This tool allows to detect all string litterals present on the Slicer python source code and mark them as translatable. It's part of the Slicer Internationalization Project **<<&nbsp;3D Slicer in my language&nbsp;>>**

## Usage syntax

To mark your strings after cloning the [Slicer main repository](https://github.com/Slicer/Slicer), run the `main.py` file and give the *Slicer* root folder as parameter :

`main.py  path/to/slicer/root/folder`

## Files

The repository is composed of three files :

 - `main.py` : the main program that run the detection and marking process on the Slicer root folder.
- `py_files_finder.py` : Python module that detects all `.py` files that are present on the `slicer source` folder and returns it as a `python list`
- `string_marker.py` : Python module that is responsible of the main logic of the program. It is responsible of marking all the detected strings on each file. The marking process is explained on the `Marking process` section
