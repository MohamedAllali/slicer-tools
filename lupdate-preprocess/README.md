# Slicer lupdate preprocessor

This script was created in the context of pull-request [Slicer#6917](https://github.com/Slicer/Slicer/pull/6917).
It allows to rewrite tr-like function calls found in Slicer scripted modules to include the context as first argument. This approach makes it possible to use pylupdate tool to extract marked strings.
It's part of the Slicer Internationalization Project **<<&nbsp;3D Slicer in my language&nbsp;>>**

## Usage syntax

To obtain a transformed your strings after cloning the [Slicer main repository](https://github.com/Slicer/Slicer), run the `main.py` file and give the *Slicer* root folder as parameter :

```lupdate_preprocess [-h] [-i INPUT] [-o OUTPUT] [-f TR_FUNCTION_NAME]

Make translation function calls compatible to lupdate needs

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file/folder name
  -o OUTPUT, --output OUTPUT
                        output file/folder name
  -f TR_FUNCTION_NAME, --funcname TR_FUNCTION_NAME
                        the translation function name (e.g. tr/translate)```

## Files

