# LangManager
Create localisations for other languages
#### Simple example:
```python
from langmanager import *

language = input('language:   ')
lang(language)
trans = translate_get('hello world')

print(lan())
print(trans)
```
And language file(ru):
```
'hello world':'привет мир';
'hello i':'привет я';
```
###### language standard file name en.txt, ru.txt, zh.txt
###### But file name can change through function filepath_en , filepath_ru and others
