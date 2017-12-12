# SynthesizeTextDetectionDatasetTool
A tool to synthesize Text Detection and Recognition Dataset. -- By Lu Dongwei(Gu Jiancheng). 

***
### Directory
- fonts(puts all fonts here for random used)
- bg(puts all background image here for random used)

### Declaration
- This tool can only synthesize square object with no rotation.

### How to use?
1. Download freetype refered to [https://github.com/rougier/freetype-py](https://github.com/rougier/freetype-py)
2. cd freetype src root directory and run cmd like "python setup.py install" to install freetype for your python(you also need to download Freetype.dll or compiled by yourself)
3. Use script Synthesize_Object_Detection_Dataset.py to synthesize dataset. You can modify parameters to meet your needs. 
4. Finally, My Project only provides necessary DLLs or Src files for windows env. Freetype is an open source tool,
for windows users, download Freetype.dll and srcfiles, move Freetype.dll to the root of python directory.
for linux or mac users, search and install with official instruction. Thank u.


***
### Some words
The code is easy to understand, if this cannot meet your needs completely, modify the codes!
If there is some errs, please contact me immediately.