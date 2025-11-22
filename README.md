# Burrows Wheeler transform
## intro/description
my (originally small) school project using the Burrows Wheeler Transform and a client-server connection, 
the og "project" was 3 files but I started adding tons of new things because I can't do something simple for once.
I'll probably add something else later but idk  

## how to use
first download zip file and extract it,
then you can run it in varous way:

please note that each command must be typed inside the "\trasformataBurrowsWheeler" folder
### 1. Manual Method
Run server.py and app.py manually IN THIS ORDER, you can use your IDE or with CMD:

to run server.py type the following command 

    python server.py

to run app.py type one of the following command 

    python app.py
or

    flask run 

Once both files are running, open a web browser and go to either
http://localhost:5000
or
http://127.0.0.1:5000

### 2. Command-Line Method
Use the command prompt (CMD) to run a single command.

    run.bat
This method allows two optional flags to customize the behavior of the program:

    -d or --debug
    -p xxxx or --port xxxx
("xxxx" must be substitued by a valid port number eg. 33333)

After running the command, the program will start automatically.

### 3. Batch File Method
Simply double-click the start.bat file.

This will automatically start everything needed for the program to run without additional steps.



## REGULAR BURROWS WHEELER TRANSFORM 

suppose that we need transform the string "banana"

STEP 1 -- add the end marker ('$' by convention) 

    "banana" --> "banana$"

STEP 2 -- rotate the string one character to the left until we return to the original string

starting with:

    "banana$"


here are all (7 including the original) possible rotations for our string: 

    "banana$"
    "anana$b"
    "nana$ba"
    "ana$ban"
    "na$bana"
    "a$banan"
    "$banana"


STEP 3 -- sort the list of strings alphabetically (using the ASCII table):

    "$banana"
    "a$banan"
    "ana$ban"
    "anana$b"
    "banana$"
    "na$bana"
    "nana$ba"


STEP 4 -- take the last character from each row

    "annb$aa"




## REVERSED BURROWS WHEELER TRANSFORM

suppose that we need to find the original word from the string "annb$aa"

STEP 1 -- append to the end of each string of the list a character of our string:

    ["a", "n", "n", "b", "$", "a", "a"]

STEP 2 -- sort the list of strings alphabetically (using the ASCII table):

    ["$", "a", "a", "a", "b", "n", "n"]

STEP 3 -- repeat until each string in the list is as long as the one we started with, the one with '$' as the last character will be the original:

    STEP 1 ["a$", "na", "na", "ba", "$b", "an", "an"]
    STEP 2 ["$b", "a$", "an", "an", "ba", "na", "na"]

    STEP 1 ["a$b", "na$", "nan", "ban", "$ba", "ana", "ana"]
    STEP 2 ["$ba", "a$b", "ana", "ana", "ban", "na$", "nan"]

    STEP 1 ["a$ba", "na$b", "nana", "bana", "$ban", "ana$", "anan"]
    STEP 2 ["$ban", "a$ba", "ana$", "anan", "bana", "na$b", "nana"]

    STEP 1 ["a$ban", "na$ba", "nana$", "banan", "$bana", "ana$b", "anana"]
    STEP 2 ["$bana", "a$ban", "ana$b", "anana", "banan", "na$ba", "nana$"]

    STEP 1 ["a$bana", "na$ban", "nana$b", "banana", "$banan", "ana$ba", "anana$"]
    STEP 2 ["$banan", "a$bana", "ana$ba", "anana$", "banana", "na$ban", "nana$b"]

    STEP 1 ["a$banan", "na$bana", "nana$ba", "banana$", "$banana", "ana$ban", "anana$b"]
    STEP 2 ["$banana", "a$banan", "ana$ban", "anana$b", "banana$", "na$bana", "nana$ba"]
