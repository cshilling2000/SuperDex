import csv

dex_filename = "natdex.csv"
alolan_forms_filename = "forms\\alola.csv"

def grab_names_and_numbers():
    names = []
    with open(dex_filename) as csvfile:
        for row in csvfile:
            names.append(row.split(',')[1].strip('\n')) 
    
    return names

def get_dex_no_from_name(names, name):
    return names.index(name) + 1

def get_name_from_no(names, no):
    return names[no-1]

def get_forms(forms_filename):
    numbers = []
    with open(forms_filename) as csvfile:
        for row in csvfile:
            numbers.append(int(row.strip('\n'))) 
 
    return numbers

def name_list_to_no_list(names):
    return range(1, len(names) + 1)

def form_mask(parent,mask):
    for element in mask:
        parent.remove(element)


