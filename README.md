# LangManager

![Image alt](https://img.shields.io/github/license/ASVIEST/LangManager?logo=GitHub&logoColor=orange&style=flat-square)
![Image alt](https://img.shields.io/discord/762602867088818218?color=green&label=server&logo=discord&logoColor=white&style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/ASVIEST/LangManager?color=green&label=size&logo=GitHub&logoColor=cAF7a6&style=flat-square)

this library allows you to create translations of projects into other languages
#### Simple example:
```python
from langmanager import *

language = input('language:   ')
lang(language)
trans = translate_get('hello world')

print(lan())
print(trans)
```
language file(en):
```
'hello world':'hello world';
```
And language file(ru):
```
'hello world':'привет мир';
```
###### language standard file name - lan(ISO 639-1).txt examples: en.txt, ru.txt, zh.txt
###### But file name can change through function filepath_en , filepath_ru and others
##### language can be changed during working
#### change filepath example:
```python
from langmanager import *

language = input('language:   ')
lang(language)
trans = translate_get('hello world')

print(lan())
print(trans)

lang(ru)
filepath_ru('en.txt')
trans = translate_get('hello i')
print(trans)
```
```
'hello world':'hello world';
'hello i':'hello i';
```
And language file(ru):
```
'hello world':'привет мир';
'hello i':'привет я';
```
