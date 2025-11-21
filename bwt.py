# abbiamo una stringa "banana"

# 1 aggiungiamo '$' alla fine 
# "banana" --> "banana$"

# 2 ruotiamo tutti i caratteri a sinistra di 1 fino a tornare al punto di partenza
# "banana$"
# "banana$" --> "anana$b"
# "anana$b" --> "nana$ba"
# "nana$ba" --> "ana$ban"
# "ana$ban" --> "na$bana"
# "na$bana" --> "a$banan"
# "a$banan" --> "$banana"

# 3 riordiniamo tuttle stringhe in ordine della tabella ascii
# "$banana"
# "a$banan"
# "ana$ban"
# "anana$b"
# "banana$"
# "na$bana"
# "nana$ba"

# 4 prendo l'ultima colonna delle stringhe ordinate dall'alto verso il basso
# "annb$aa"

# Sorting fatto con il QuickSort 
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def trasformata(input:str):
    # STEP 1
    input += '$'
    # dichiarazione
    listaSuCuiStoLavorando = [None] * len(input)
    strTrasformata = ""
    # STEP 2
    listaSuCuiStoLavorando[0] = input
    for x in range(1,len(input)):
        listaSuCuiStoLavorando[x] = listaSuCuiStoLavorando[x-1][1:len(input)] + listaSuCuiStoLavorando[x-1][0]
    # STEP 3
    quick_sort(listaSuCuiStoLavorando, 0, len(listaSuCuiStoLavorando) - 1)
    # STEP 4
    for x in listaSuCuiStoLavorando:
        strTrasformata += x[-1]
    return strTrasformata


def deTrasformata(input:str):
    listaSuCuiStoLavorando = [""] * len(input)
    strDeTrasformata = ""
    for i in range(len(input)):
        for j in range(len(input)):
            listaSuCuiStoLavorando[j] = input[j] + listaSuCuiStoLavorando[j]
        quick_sort(listaSuCuiStoLavorando, 0, len(listaSuCuiStoLavorando) - 1)
        
    for x in listaSuCuiStoLavorando:
        if x[0] == "$":
            strDeTrasformata = x
    return strDeTrasformata

