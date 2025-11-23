# Burrows Wheeler transform
## intro/description
This is my school project implementing the Burrows–Wheeler Transform and a simple client–server architecture.

The original project was just three files, but I kept adding new features because I can’t keep things simple.

I'll probably add something else later but idk

## how to use
Download the ZIP file and extract it.

please note that each command must be typed inside the `\trasformataBurrowsWheeler` folder
### 1. Manual Method
Run `server.py` and `app.py`

to run `server.py` type the following command:
```
python server.py
```
to run `app.py` type the following command:
```
python app.py
```
Once both are running, open a web browser and go to either
http://localhost:5000
or
http://127.0.0.1:5000

### 2. Command-Line Method
Use the command prompt (CMD) to run the included batch script.
```
start.bat
```
This method allows two optional flags:
```
-d or --debug
-p xxxx or --port xxxx
```
("xxxx" must be substitued by a valid port number eg. 33333)

After running the command, the program will start automatically.

### 3. Batch File Method
Just double-click the `start.bat` file.

This will automatically start everything needed for the program to run without additional steps.



## REGULAR BURROWS WHEELER TRANSFORM 

suppose that we need transform the following string:
```
"banana"
```
STEP 1 -- add the end marker ('$' by convention):
```
"banana$"
```
STEP 2 -- generate all possible rotation of the string:
```
"banana$"
"anana$b"
"nana$ba"
"ana$ban"
"na$bana"
"a$banan"
"$banana"
```
STEP 3 -- sort the list of strings alphabetically (using the ASCII table):
```
"$banana"
"a$banan"
"ana$ban"
"anana$b"
"banana$"
"na$bana"
"nana$ba"
```
STEP 4 -- take the last character from each row, this will be the transformed string:
```
"annb$aa"
```



## REVERSED BURROWS WHEELER TRANSFORM

suppose that we need to find the original word from the string "annb$aa"

STEP 1 -- append to each string of the list a character of our string:
```
["a", "n", "n", "b", "$", "a", "a"]
```
STEP 2 -- sort the list alphabetically (using the ASCII table):
```
["$", "a", "a", "a", "b", "n", "n"]
```
STEP 3 -- repeat the previous steps:
```
["a$", "na", "na", "ba", "$b", "an", "an"]
["$b", "a$", "an", "an", "ba", "na", "na"]
```
```
["a$b", "na$", "nan", "ban", "$ba", "ana", "ana"]
["$ba", "a$b", "ana", "ana", "ban", "na$", "nan"]
```
```
["a$ba", "na$b", "nana", "bana", "$ban", "ana$", "anan"]
["$ban", "a$ba", "ana$", "anan", "bana", "na$b", "nana"]
```
```
["a$ban", "na$ba", "nana$", "banan", "$bana", "ana$b", "anana"]
["$bana", "a$ban", "ana$b", "anana", "banan", "na$ba", "nana$"]
```
```
["a$bana", "na$ban", "nana$b", "banana", "$banan", "ana$ba", "anana$"]
["$banan", "a$bana", "ana$ba", "anana$", "banana", "na$ban", "nana$b"]
```
```
["a$banan", "na$bana", "nana$ba", "banana$", "$banana", "ana$ban", "anana$b"]
["$banana", "a$banan", "ana$ban", "anana$b", "banana$", "na$bana", "nana$ba"]
```
STEP 4 -- the element that ends with '$' will be the original string:
```
"banana$"
```
