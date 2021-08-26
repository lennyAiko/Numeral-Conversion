# TO DECIDE EACH NUMBER
from items import *


# UNIT
def singles(num):
    i = int(num)
    value = SINGLE_VALUES[i]
    return value


# TENS
def doubles(num):
    store = []
    array = UNIT[int(num[0])]
    for i in num:
        value = singles(i)
        store.append(value)
    query = store[0] + " " + store[1]
    return array[query]


# HUNDREDS
def triples(num):
    first = int(num[0])
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        second_store.append(i)
        store.append(value)
    number = singles(first)
    if store[1] == "zero" and store[2] == "zero":
        word = f'{number.capitalize()} hundred'
    elif store[1] == "zero":
        last = singles(second_store[2])
        word = f'{number.capitalize()} hundred and {last}'
    else:
        last = doubles(second_store[1:])
        word = f'{number.capitalize()} hundred and {last}'
    return word


# THOUSANDS
def quadruples(num):
    first = int(num[0])
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = singles(first)
    if store[1] == "zero" and store[2] == "zero" and store[3] == "zero":
        word = f'{number.capitalize()} thousand'
    elif store[1] == "zero" and store[2] == "zero":
        last = singles(second_store[3])
        word = f'{number.capitalize()} thousand, and {last}'
    elif store[1] == "zero":
        last = doubles(second_store[2:])
        word = f'{number.capitalize()} thousand, and {last}'
    else:
        last = triples(second_store[1:])
        word = f'{number.capitalize()} thousand, {last}'
    return word


# TENTH THOUSAND
def pentas(num):
    first = num[:2]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = doubles(first)
    if store[2] == "zero" and store[3] == "zero" and store[4] == "zero":
        word = f'{number.capitalize()} thousand'
    elif store[2] == "zero" and store[3] == "zero":
        last = singles(second_store[4])
        word = f'{number.capitalize()} thousand, and {last}'
    elif store[2] == "zero":
        last = doubles(second_store[3:])
        word = f'{number.capitalize()} thousand, and {last}'
    else:
        last = triples(second_store[2:])
        word = f'{number.capitalize()} thousand, {last}'
    return word


# HUNDREDTH THOUSAND
def hexas(num):
    first = num[:3]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = triples(first)
    if store[3] == "zero" and store[4] == "zero" and store[5] == "zero":
        word = f'{number.capitalize()} Thousand'
    elif store[3] == "zero" and store[4] == "zero":
        last = singles(second_store[5])
        word = f'{number.capitalize()} thousand, and {last}'
    elif store[3] == "zero":
        last = doubles(second_store[4:])
        word = f'{number.capitalize()} thousand, and {last}'
    else:
        last = triples(second_store[3:])
        word = f'{number.capitalize()} thousand, {last}'
    return word


# MILLION
def heptas(num):
    first = num[0]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = singles(first)
    if (store[1] == "zero" and store[2] == "zero" and
            store[3] == "zero" and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"):
        word = f'{number.capitalize()} Million'
    elif store[1] == "zero" and store[2] == "zero" and store[3] == "zero" and store[4] == "zero" and store[5] == "zero":
        last = singles(second_store[6])
        word = f'{number.capitalize()} Million, and {last}'
    elif store[1] == "zero" and store[2] == "zero" and store[3] == "zero" and store[4] == "zero":
        last = doubles(second_store[5:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[1] == "zero" and store[2] == "zero" and store[3] == "zero":
        last = triples(second_store[4:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[1] == "zero" and store[2] == "zero":
        last = quadruples(second_store[3:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[1] == "zero":
        last = pentas(second_store[2:])
        word = f'{number.capitalize()} Million, {last}'
    else:
        last = hexas(second_store[1:])
        word = f'{number.capitalize()} Million, {last}'
    return word


# TENTH MILLION
def octas(num):
    first = num[:2]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = doubles(first)
    if (store[2] == "zero" and
            store[3] == "zero" and store[4] == "zero"
            and store[5] == "zero" and store[6] == "zero" and store[7] == "zero"):
        word = f'{number.capitalize()} Million'
    elif store[2] == "zero" and store[3] == "zero" and store[4] == "zero" and store[5] == "zero" and store[6] == "zero":
        last = singles(second_store[7])
        word = f'{number.capitalize()} Million, and {last}'
    elif store[2] == "zero" and store[3] == "zero" and store[4] == "zero" and store[5] == "zero":
        last = doubles(second_store[6:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[2] == "zero" and store[3] == "zero" and store[4] == "zero":
        last = triples(second_store[5:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[2] == "zero" and store[3] == "zero":
        last = quadruples(second_store[4:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[2] == "zero":
        last = pentas(second_store[3:])
        word = f'{number.capitalize()} Million, {last}'
    else:
        last = hexas(second_store[2:])
        word = f'{number.capitalize()} Million, {last}'
    return word


# HUNDREDTH MILLION
def nonas(num):
    first = num[:3]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = triples(first)
    if (store[3] == "zero" and
            store[4] == "zero" and store[5] == "zero"
            and store[6] == "zero" and store[7] == "zero" and store[8] == "zero"):
        word = f'{number.capitalize()} Million'
    elif store[3] == "zero" and store[4] == "zero" and store[5] == "zero" and store[6] == "zero" and store[7] == "zero":
        last = singles(second_store[8])
        word = f'{number.capitalize()} Million, and {last}'
    elif store[3] == "zero" and store[4] == "zero" and store[5] == "zero" and store[6] == "zero":
        last = doubles(second_store[7:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[3] == "zero" and store[4] == "zero" and store[5] == "zero":
        last = triples(second_store[6:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[3] == "zero" and store[4] == "zero":
        last = quadruples(second_store[5:])
        word = f'{number.capitalize()} Million, {last}'
    elif store[3] == "zero":
        last = pentas(second_store[4:])
        word = f'{number.capitalize()} Million, {last}'
    else:
        last = hexas(second_store[3:])
        word = f'{number.capitalize()} Million, {last}'
    return word


# BILLION
def decas(num):
    first = num[0]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = singles(first)
    if (store[1] == "zero" and store[2] == "zero" and store[3] == "zero"
            and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
            and store[7] == "zero" and store[8] == "zero" and store[9] == "zero"):
        word = f'{number.capitalize()} Billion'
    elif (store[1] == "zero" and store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero" and store[8] == "zero"):
        last = singles(second_store[9])
        word = f'{number.capitalize()} Billion, and {last}'
    elif (store[1] == "zero" and store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero" and store[7] == "zero"):
        last = doubles(second_store[8:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[1] == "zero" and store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"):
        last = triples(second_store[7:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[1] == "zero" and store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero"):
        last = quadruples(second_store[6:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[1] == "zero" and store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero"):
        last = pentas(second_store[5:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[1] == "zero" and store[2] == "zero" and store[3] == "zero":
        last = hexas(second_store[4:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[1] == "zero" and store[2] == "zero":
        last = heptas(second_store[3:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[1] == "zero":
        last = octas(second_store[2:])
        word = f'{number.capitalize()} Billion, {last}'
    else:
        last = nonas(second_store[1:])
        word = f'{number.capitalize()} Billion, {last}'
    return word


# TENTH BILLION
def elevens(num):
    first = num[:2]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = doubles(first)
    if (store[2] == "zero" and store[3] == "zero"
            and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
            and store[7] == "zero" and store[8] == "zero" and store[9] == "zero"
            and store[10] == "zero"):
        word = f'{number.capitalize()} Billion'
    elif (store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero" and store[8] == "zero" and store[9] == "zero"):
        last = singles(second_store[10])
        word = f'{number.capitalize()} Billion, and {last}'
    elif (store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero" and store[8] == "zero"):
        last = doubles(second_store[9:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero"):
        last = triples(second_store[8:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"):
        last = quadruples(second_store[7:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[2] == "zero" and store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero"):
        last = pentas(second_store[6:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[2] == "zero" and store[3] == "zero" and store[4] == "zero":
        last = hexas(second_store[5:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[2] == "zero" and store[3] == "zero":
        last = heptas(second_store[4:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[2] == "zero":
        last = octas(second_store[3:])
        word = f'{number.capitalize()} Billion, {last}'
    else:
        last = nonas(second_store[2:])
        word = f'{number.capitalize()} Billion, {last}'
    return word


# HUNDRED BILLION
def twelves(num):
    first = num[:3]
    store = []
    second_store = []
    for i in num:
        value = singles(i)
        store.append(value)
        second_store.append(i)
    number = triples(first)
    if (store[3] == "zero"
            and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
            and store[7] == "zero" and store[8] == "zero" and store[9] == "zero"
            and store[10] == "zero" and store[11] == "zero"):
        word = f'{number.capitalize()} Billion'
    elif (store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero" and store[8] == "zero" and store[9] == "zero" and store[10] == "zero"):
        last = singles(second_store[11])
        word = f'{number.capitalize()} Billion, and {last}'
    elif (store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero" and store[8] == "zero" and store[9] == "zero"):
        last = doubles(second_store[10:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"
          and store[7] == "zero" and store[8] == "zero"):
        last = triples(second_store[9:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero" and store[7] == "zero"):
        last = quadruples(second_store[8:])
        word = f'{number.capitalize()} Billion, {last}'
    elif (store[3] == "zero"
          and store[4] == "zero" and store[5] == "zero" and store[6] == "zero"):
        last = pentas(second_store[7:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[3] == "zero" and store[4] == "zero" and store[5] == "zero":
        last = hexas(second_store[6:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[3] == "zero" and store[4] == "zero":
        last = heptas(second_store[5:])
        word = f'{number.capitalize()} Billion, {last}'
    elif store[3] == "zero":
        last = octas(second_store[4:])
        word = f'{number.capitalize()} Billion, {last}'
    else:
        last = nonas(second_store[3:])
        word = f'{number.capitalize()} Billion, {last}'
    return word


COUNT = [singles, doubles, triples, quadruples, pentas, hexas, heptas, octas, nonas, decas, elevens, twelves]


def decide(num):
    i = len(num) - 1
    value = COUNT[i]
    return value
