# trasformataBurrowsWheeler
my "web app" for a school project using the Burrows Wheeler Transform and a client-server connection




this is the section where is explained how does the Burrows Wheeler Transform works and how to reverse it

### REGULAR BURROWS WHEELER TRANSFORM ####

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




### REVERSED BURROWS WHEELER TRANSFORM ####

suppose that we need to find the original word from the string "annb$aa"

STEP 1 -- append to the end of each string of the list a character of our string
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