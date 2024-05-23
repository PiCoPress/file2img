# FIMMPY - Visualize any file
## Dependencies
1. PIL
2. numpy

## Usage
```py
import fimmpy

fimmpy.visualize(file: str, out: str, plt: int)
```
`file`: A file to convert
`out`: Destination of image
`plt`: Palette byte size, default is 4, allowed 1, 2, 3, and 4

## Example
Visualized 24bit RGB [`Hello-C-World-main.zip`](https://github.com/pr0gr4m/Hello-C-World) is;  

![Converted Image](./output.png) 
