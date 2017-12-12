# SynthesizeTextDetectionDatasetTool
A tool to synthesize Text Detection and Recognition Dataset. -- By Lu Dongwei(Gu Jiancheng). 

***
### Directory
- fonts(puts all fonts here for random used)
- bg(puts all background image here for random used)

### Declaration
- This tool can only synthesize square object with no rotation.

### How to use?
#### Windows env
1.
```
git clone https://github.com/yzldw333/SynthesizeTextDetectionDatasetTool.git
```
2. move *Freetype.dll* to the root of python directory(or Anaconda directory)
3. unzip *freetype-py-master.zip*
```
cd freetype-py-master
python setup.py install
```
4. test if you can **import freetype** successfully.
5. use script *Synthesize_Object_Detection_Dataset.py* to synthesize dataset. You can modify parameters to meet your needs


#### General use method
1. unzip *freetype-py-master.zip* or Download freetype source file, from [https://github.com/rougier/freetype-py](https://github.com/rougier/freetype-py)
```
cd freetype-py-master
python setup.py install
```
2. Go to official [freetype website](https://www.freetype.org/) to download source files or precompiled dlls.
3. Use script Synthesize_Object_Detection_Dataset.py to synthesize dataset. You can modify parameters to meet your needs. 


***
### Some words
The code is easy to understand, if this cannot meet your needs completely, modify the codes!
If there is some errs, please contact me immediately.
