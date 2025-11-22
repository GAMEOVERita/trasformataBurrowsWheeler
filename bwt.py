import quickSort
def bwt(input_str:str):
    # STEP 1 
    # append an end marker ('$' by convention)
    input_str += '$'

    # STEP 2 
    # build all rotations of the original string
    rotations = [input_str[i:] + input_str[:i] for i in range(len(input_str))]

    # STEP 3 
    # sort all rotation in alphabetical order 
    quickSort.qSort(rotations, 0, len(rotations) - 1)

    # STEP 4 
    # put the last character of each rotation in the last column
    result = ''.join(row[-1] for row in rotations)
    return result

#reverse BWT
def reverse_bwt(input_str:str):
    # assign size variable and create a empty table to store all strings while rebuilding the original
    size = len(input_str)
    table = [""] * size

    # adds the character and sort the table until it's complete
    for _i in range(size):
        table = [input_str[j] + table[j] for j in range(size)]
        quickSort.qSort(table, 0, len(table) - 1)
        
    # finds which element of the table ends with '$' and returns it without '$'
    for elem in table:
        if elem[-1] == "$":
            return elem[:-1]
    return ""


if __name__ == "__main__":
    print(bwt("banana"))
    print(reverse_bwt(bwt("banana")))
